const motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");

const revealGroups = [
  [".capabilities span", "chip"],
  [".section-heading > *", "text"],
  [".lead-case", "panel"],
  [".case-meta > *", "text"],
  [".lead-case-visual", "image"],
  [".case-story section", "panel"],
  [".process-line li", "chip"],
  [".process-visual", "image"],
  [".case-card", "panel"],
  [".timeline article", "panel"],
  [".tool-grid article", "panel"],
  [".contact > *", "text"],
  ["address a", "chip"],
];

function base64ToBlob(base64, mime) {
  const binary = window.atob(base64);
  const chunks = [];

  for (let index = 0; index < binary.length; index += 1024) {
    const slice = binary.slice(index, index + 1024);
    const bytes = new Uint8Array(slice.length);
    for (let byteIndex = 0; byteIndex < slice.length; byteIndex += 1) {
      bytes[byteIndex] = slice.charCodeAt(byteIndex);
    }
    chunks.push(bytes);
  }

  return new Blob(chunks, { type: mime });
}

function prepareResumeDownload() {
  const payload = window.resumeDownloadPayload;
  if (!payload?.base64) return;

  document.querySelectorAll(".resume-download").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();

      const blob = base64ToBlob(payload.base64, payload.mime || "text/markdown");
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");

      anchor.href = url;
      anchor.download = payload.filename || link.getAttribute("download") || "resume.md";
      anchor.style.display = "none";
      document.body.append(anchor);
      anchor.click();
      anchor.remove();

      window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    });
  });
}

function prepareReveals() {
  document.documentElement.classList.add("js-enabled");

  revealGroups.forEach(([selector, motion]) => {
    document.querySelectorAll(selector).forEach((element, index) => {
      element.classList.add("reveal");
      element.dataset.motion = motion;
      element.style.setProperty("--reveal-delay", `${Math.min(index * 90, 360)}ms`);
    });
  });
}

function revealImmediately() {
  document.querySelectorAll(".reveal").forEach((element) => {
    element.classList.add("is-visible");
  });
}

function revealHashTarget() {
  if (!window.location.hash) return;

  const targetId = decodeURIComponent(window.location.hash.slice(1));
  const target = document.getElementById(targetId);
  if (!target) return;

  if (target.classList.contains("reveal")) {
    target.classList.add("is-visible");
  }

  target.querySelectorAll(".reveal").forEach((element) => {
    element.classList.add("is-visible");
  });
}

function observeReveals() {
  if (!("IntersectionObserver" in window)) {
    revealImmediately();
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      rootMargin: "0px 0px -12% 0px",
      threshold: 0.16,
    },
  );

  document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
}

prepareResumeDownload();
prepareReveals();

if (motionQuery.matches) {
  revealImmediately();
} else {
  observeReveals();
  revealHashTarget();
  window.addEventListener("hashchange", revealHashTarget);
}
