(function () {
  "use strict";

  const BY_LECTURE = window.CP650_MCQS_BY_LECTURE;
  if (!BY_LECTURE || typeof BY_LECTURE !== "object") {
    document.body.innerHTML =
      "<p style=\"padding:2rem;font-family:system-ui\">Error: mcqs-data.js did not load. Keep index.html, app.js, and mcqs-data.js in the same folder.</p>";
    return;
  }

  const STORAGE_KEY_WRONG = "cp650_wrong_mcqs";

  const LECTURE_TITLES = {
    1: "Ch.1 — Multidisciplinary interaction design",
    2: "Design principles & accessibility",
    3: "The process of interaction design",
    4: "Conceptualizing interaction design",
    5: "Cognitive aspects",
    6: "Social interaction",
    7: "Emotional interaction",
    8: "Interface types",
    9: "Data gathering I",
    10: "Data gathering II (ontology, validity, sampling, ethics)",
    11: "Qualitative data analysis",
    12: "Field studies & analysis frameworks",
    13: "Discovering requirements",
    14: "Data at scale",
    15: "Ideate, design, prototyping & construction",
  };

  let DATA = [];
  let currentLecture = null;
  let order = [];
  let index = 0;
  let answered = false;
  let correctCount = 0;
  let attempted = 0;

  const pickerView = document.getElementById("pickerView");
  const quizView = document.getElementById("quizView");
  const lectureGrid = document.getElementById("lectureGrid");
  const backBtn = document.getElementById("backBtn");
  const lectureBadge = document.getElementById("lectureBadge");
  const questionText = document.getElementById("questionText");
  const questionMeta = document.getElementById("questionMeta");
  const optionsRoot = document.getElementById("optionsRoot");
  const feedback = document.getElementById("feedback");
  const nextBtn = document.getElementById("nextBtn");
  const progressText = document.getElementById("progressText");
  const scoreText = document.getElementById("scoreText");
  const shuffleToggle = document.getElementById("shuffleToggle");
  const filterAnalytical = document.getElementById("filterAnalytical");
  const restartBtn = document.getElementById("restartBtn");
  const wrongCountEl = document.getElementById("wrongCount");
  const btnWrongReview = document.getElementById("btnWrongReview");
  const btnWrongClear = document.getElementById("btnWrongClear");
  const wrongReviewPanel = document.getElementById("wrongReviewPanel");
  const wrongReviewList = document.getElementById("wrongReviewList");

  function loadWrongList() {
    try {
      const raw = sessionStorage.getItem(STORAGE_KEY_WRONG);
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  function saveWrongList(list) {
    sessionStorage.setItem(STORAGE_KEY_WRONG, JSON.stringify(list));
  }

  function wrongRecordKey(rec) {
    return `${rec.lecture}\n${rec.question}\n${rec.correct}`;
  }

  function appendWrongRecord(item, selectedIdx) {
    if (currentLecture == null) return;
    const rec = {
      lecture: currentLecture,
      question: stripTags(item.q),
      picked: item.options[selectedIdx],
      correct: item.options[item.correct],
      cat: item.cat || "recall",
      at: new Date().toISOString(),
    };
    const list = loadWrongList();
    const k = wrongRecordKey(rec);
    if (list.some((r) => wrongRecordKey(r) === k)) {
      updateWrongUI();
      return;
    }
    list.push(rec);
    saveWrongList(list);
    updateWrongUI();
  }

  function updateWrongUI() {
    const list = loadWrongList();
    const n = list.length;
    wrongCountEl.textContent = String(n);
    btnWrongReview.disabled = n === 0;
    wrongReviewList.innerHTML = "";
    for (let i = list.length - 1; i >= 0; i--) {
      const r = list[i];
      const li = document.createElement("li");
      const title = LECTURE_TITLES[r.lecture] || "Lecture " + r.lecture;
      li.innerHTML = `<span class="wrong-li-meta">L${r.lecture} · ${escapeHtml(r.cat)} · ${escapeHtml(title)}</span>` +
        `<span class="wrong-li-q">${escapeHtml(r.question)}</span>` +
        `<span class="wrong-li-picked">You: ${escapeHtml(r.picked)}</span>` +
        `<span class="wrong-li-correct">Correct: ${escapeHtml(r.correct)}</span>`;
      wrongReviewList.appendChild(li);
    }
  }

  function escapeHtml(s) {
    const d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  function shuffleArray(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function stripTags(q) {
    return q
      .replace(/^\[L\d+\]\s*/i, "")
      .replace(/^\(\d+\)\s*/, "")
      .replace(/\s*\(v\d+\)\s*$/, "")
      .trim();
  }

  function buildOrder() {
    let indices = DATA.map((_, i) => i);
    if (filterAnalytical.checked) {
      const filtered = indices.filter(
        (i) => DATA[i].cat === "analysis" || DATA[i].cat === "application"
      );
      if (filtered.length > 0) indices = filtered;
    }
    order = shuffleToggle.checked ? shuffleArray(indices) : indices;
    index = 0;
    answered = false;
    correctCount = 0;
    attempted = 0;
  }

  function showPicker() {
    currentLecture = null;
    pickerView.classList.remove("hidden");
    quizView.classList.add("hidden");
    quizView.setAttribute("aria-hidden", "true");
  }

  function startLecture(num) {
    const key = String(num);
    const list = BY_LECTURE[key];
    if (!Array.isArray(list) || list.length === 0) {
      alert("No questions loaded for Lecture " + key + ". Regenerate mcqs-data.js.");
      return;
    }
    currentLecture = num;
    DATA = list;
    lectureBadge.textContent = "Lecture " + key + " · " + (LECTURE_TITLES[num] || "");
    pickerView.classList.add("hidden");
    quizView.classList.remove("hidden");
    quizView.setAttribute("aria-hidden", "false");
    buildOrder();
    renderQuestion();
  }

  function renderQuestion() {
    if (!DATA.length) return;
    answered = false;
    feedback.classList.add("hidden");
    feedback.textContent = "";
    feedback.classList.remove("ok", "bad");
    nextBtn.classList.add("hidden");
    nextBtn.disabled = true;

    const qi = order[index];
    const item = DATA[qi];
    const qClean = stripTags(item.q);

    const cat = item.cat || "recall";
    questionMeta.textContent = cat === "recall" ? "Recall" : cat === "application" ? "Application" : "Analysis";
    questionText.textContent = qClean;
    optionsRoot.innerHTML = "";

    item.options.forEach((label, optIdx) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "option-btn";
      btn.textContent = label;
      btn.setAttribute("role", "radio");
      btn.addEventListener("click", () => onSelect(optIdx, item, btn));
      optionsRoot.appendChild(btn);
    });

    const total = order.length;
    progressText.textContent = `Question ${index + 1} of ${total}`;
    scoreText.textContent = `Score: ${correctCount} / ${attempted}`;
  }

  function onSelect(selectedIdx, item) {
    if (answered) return;
    answered = true;
    attempted += 1;

    const isCorrect = selectedIdx === item.correct;
    if (isCorrect) correctCount += 1;

    const buttons = optionsRoot.querySelectorAll(".option-btn");
    buttons.forEach((btn, i) => {
      btn.disabled = true;
      if (i === item.correct) {
        btn.classList.add("correct");
      } else if (i === selectedIdx && !isCorrect) {
        btn.classList.add("wrong");
      } else {
        btn.classList.add("neutral-disabled");
      }
    });

    feedback.classList.remove("hidden");
    if (isCorrect) {
      feedback.classList.add("ok");
      feedback.classList.remove("bad");
      feedback.textContent = "Correct.";
    } else {
      feedback.classList.add("bad");
      feedback.classList.remove("ok");
      const rightLabel = item.options[item.correct];
      feedback.textContent = `Wrong. The best answer is: ${rightLabel}`;
      appendWrongRecord(item, selectedIdx);
    }

    scoreText.textContent = `Score: ${correctCount} / ${attempted}`;

    nextBtn.classList.remove("hidden");
    nextBtn.disabled = false;
    nextBtn.focus();
  }

  function nextQuestion() {
    if (index < order.length - 1) {
      index += 1;
      renderQuestion();
    } else {
      questionMeta.textContent = "Done";
      questionText.textContent = "You finished this run.";
      optionsRoot.innerHTML = "";
      feedback.classList.remove("hidden");
      feedback.classList.remove("bad");
      feedback.classList.add("ok");
      feedback.textContent = `Final score: ${correctCount} out of ${attempted} answered (${order.length} questions in this set). Use Restart or pick another lecture.`;
      nextBtn.classList.add("hidden");
      progressText.textContent = "Complete";
    }
  }

  function initPicker() {
    for (let n = 1; n <= 15; n++) {
      const key = String(n);
      const list = BY_LECTURE[key];
      const count = Array.isArray(list) ? list.length : 0;
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "lecture-tile";
      btn.innerHTML = `<span class="tile-num">${n}</span><span class="tile-title">${LECTURE_TITLES[n] || "Lecture " + n}</span><span class="tile-count">${count} MCQs</span>`;
      btn.disabled = count === 0;
      btn.addEventListener("click", () => startLecture(n));
      lectureGrid.appendChild(btn);
    }
  }

  nextBtn.addEventListener("click", nextQuestion);

  backBtn.addEventListener("click", () => {
    showPicker();
  });

  restartBtn.addEventListener("click", () => {
    buildOrder();
    renderQuestion();
  });

  shuffleToggle.addEventListener("change", () => {
    buildOrder();
    renderQuestion();
  });

  filterAnalytical.addEventListener("change", () => {
    buildOrder();
    renderQuestion();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !nextBtn.classList.contains("hidden") && !nextBtn.disabled) {
      nextQuestion();
    }
  });

  btnWrongReview.addEventListener("click", () => {
    wrongReviewPanel.classList.toggle("hidden");
    if (!wrongReviewPanel.classList.contains("hidden")) {
      updateWrongUI();
    }
  });

  btnWrongClear.addEventListener("click", () => {
    saveWrongList([]);
    updateWrongUI();
    wrongReviewPanel.classList.add("hidden");
  });

  initPicker();
  updateWrongUI();
  showPicker();
})();
