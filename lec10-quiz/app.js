(function () {
  "use strict";

  const DATA = window.LEC10_MCQS;
  if (!Array.isArray(DATA) || DATA.length === 0) {
    document.getElementById("questionText").textContent =
      "Error: lec10-mcqs.js did not load. Keep index.html, app.js, and lec10-mcqs.js in the same folder.";
    return;
  }

  let order = [];
  let index = 0;
  let answered = false;
  let correctCount = 0;
  let attempted = 0;

  const questionText = document.getElementById("questionText");
  const optionsRoot = document.getElementById("optionsRoot");
  const feedback = document.getElementById("feedback");
  const nextBtn = document.getElementById("nextBtn");
  const progressText = document.getElementById("progressText");
  const scoreText = document.getElementById("scoreText");
  const shuffleToggle = document.getElementById("shuffleToggle");
  const restartBtn = document.getElementById("restartBtn");

  function shuffleArray(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function buildOrder() {
    const indices = DATA.map((_, i) => i);
    order = shuffleToggle.checked ? shuffleArray(indices) : indices;
    index = 0;
    answered = false;
    correctCount = 0;
    attempted = 0;
  }

  function stripLeadingNumber(q) {
    return q.replace(/^\(\d+\)\s*/, "").trim();
  }

  function renderQuestion() {
    answered = false;
    feedback.classList.add("hidden");
    feedback.textContent = "";
    feedback.classList.remove("ok", "bad");
    nextBtn.classList.add("hidden");
    nextBtn.disabled = true;

    const qi = order[index];
    const item = DATA[qi];
    const qClean = stripLeadingNumber(item.q);

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

  function onSelect(selectedIdx, item, clickedBtn) {
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
      questionText.textContent = "You finished this run.";
      optionsRoot.innerHTML = "";
      feedback.classList.remove("hidden");
      feedback.classList.remove("bad");
      feedback.classList.add("ok");
      feedback.textContent = `Final score: ${correctCount} out of ${attempted} answered (${order.length} questions in this set). Use Restart for another pass.`;
      nextBtn.classList.add("hidden");
      progressText.textContent = "Complete";
    }
  }

  nextBtn.addEventListener("click", nextQuestion);

  restartBtn.addEventListener("click", () => {
    buildOrder();
    renderQuestion();
  });

  shuffleToggle.addEventListener("change", () => {
    buildOrder();
    renderQuestion();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !nextBtn.classList.contains("hidden") && !nextBtn.disabled) {
      nextQuestion();
    }
  });

  buildOrder();
  renderQuestion();
})();
