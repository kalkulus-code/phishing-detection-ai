const form = document.querySelector("#email-form");
const subjectField = document.querySelector("#subject");
const bodyField = document.querySelector("#body");
const modelPresence = document.querySelector("#model-presence");
const modelPresenceText = document.querySelector("#model-presence-text");
const analyzeButton = document.querySelector("#analyze-button");
const report = document.querySelector("#report");
const reportState = document.querySelector("#report-state");
const emptyReport = document.querySelector("#empty-report");
const emptyReportTitle = document.querySelector("#empty-report-title");
const emptyReportCopy = document.querySelector("#empty-report-copy");
const analysisResult = document.querySelector("#analysis-result");
const reportError = document.querySelector("#report-error");
const editorError = document.querySelector("#editor-error");
const resetButton = document.querySelector("#reset-button");
const characterCount = document.querySelector("#character-count");
const themeToggle = document.querySelector("#theme-toggle");
const themeToggleLabel = document.querySelector("#theme-toggle-label");
const sampleSubject = "Verifikasi akses Anda hari ini";
const sampleBody = `Halo,\n\nAktivitas pada akun Anda memerlukan konfirmasi. Perbarui akses melalui tautan berikut sebelum pukul 18.00:\nhttps://akun-contoh.example/verifikasi\n\nJika Anda tidak meminta pembaruan ini, abaikan pesan ini.\n\nSalam,\nTim Contoh`;

const numberFormat = new Intl.NumberFormat("id-ID");
const percentFormat = new Intl.NumberFormat("id-ID", {
  style: "percent",
  maximumFractionDigits: 1,
});

function applyTheme(theme, save = true) {
  const isDark = theme === "dark";
  document.documentElement.dataset.theme = isDark ? "dark" : "light";
  themeToggle.setAttribute("aria-pressed", String(isDark));
  themeToggle.setAttribute("aria-label", isDark ? "Aktifkan mode terang" : "Aktifkan mode gelap");
  themeToggleLabel.textContent = isDark ? "Terang" : "Gelap";
  document.querySelector('meta[name="theme-color"]').content = isDark ? "#101914" : "#173f32";

  if (save) {
    try {
      localStorage.setItem("saring-theme", isDark ? "dark" : "light");
    } catch {
      // The selection still applies for this page view.
    }
  }
}

applyTheme(document.documentElement.dataset.theme === "dark" ? "dark" : "light", false);
themeToggle.addEventListener("click", () => {
  applyTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark");
});

function updateCharacterCount() {
  const length = subjectField.value.length + bodyField.value.length;
  characterCount.textContent = `${numberFormat.format(length)} / 50.000`;
  characterCount.classList.toggle("is-over-limit", length > 50_000);
  resetButton.disabled = report.getAttribute("aria-busy") === "true"
    || (length === 0 && analysisResult.hidden && reportError.hidden && editorError.hidden);
}

function handleDraftChange() {
  const hadResult = !analysisResult.hidden;
  const hadError = !reportError.hidden || !editorError.hidden;
  clearMessages();

  if (hadResult) {
    analysisResult.hidden = true;
    analysisResult.classList.remove("is-entering");
    emptyReport.hidden = false;
    emptyReportTitle.textContent = "Email berubah.";
    emptyReportCopy.textContent = "Jalankan analisis ulang agar hasil sesuai dengan isi terbaru.";
    reportState.textContent = "Perlu analisis ulang";
  } else if (hadError) {
    emptyReport.hidden = false;
    emptyReportTitle.textContent = "Belum ada hasil.";
    emptyReportCopy.textContent = "Klasifikasi dan sinyal yang terukur akan muncul di sini setelah email dianalisis.";
    reportState.textContent = "Menunggu email";
  }

  updateCharacterCount();
}

function clearMessages() {
  editorError.hidden = true;
  editorError.textContent = "";
  reportError.hidden = true;
  reportError.textContent = "";
}

function setModelPresence(state, message) {
  modelPresence.dataset.state = state;
  modelPresenceText.textContent = message;
}

async function checkModel() {
  try {
    const response = await fetch("/api/health", { headers: { Accept: "application/json" } });
    if (!response.ok) throw new Error("Server tidak merespons.");

    const status = await response.json();
    if (status.ready) {
      setModelPresence("ready", "Berkas model tersedia");
    } else {
      setModelPresence("missing", "Berkas model tidak ditemukan");
    }
  } catch {
    setModelPresence("offline", "Server model tidak terhubung");
  }
}

function setBusy(isBusy) {
  report.setAttribute("aria-busy", String(isBusy));
  analyzeButton.disabled = isBusy;
  analyzeButton.textContent = isBusy ? "Menganalisis…" : "Analisis email";
  subjectField.disabled = isBusy;
  bodyField.disabled = isBusy;
  document.querySelector("#load-sample").disabled = isBusy;
  updateCharacterCount();
}

function formatSignal(value) {
  if (typeof value === "boolean") return value ? "Ya" : "Tidak";
  if (typeof value === "number") return numberFormat.format(value);
  return String(value);
}

function renderSignals(signals) {
  const list = document.querySelector("#signal-list");
  const fragment = document.createDocumentFragment();

  for (const signal of signals) {
    const row = document.createElement("div");
    row.className = "signal-row";

    const name = document.createElement("dt");
    name.textContent = signal.name;

    const value = document.createElement("dd");
    value.textContent = formatSignal(signal.value);

    row.append(name, value);
    fragment.append(row);
  }

  list.replaceChildren(fragment);
}

function renderUrls(urls) {
  const list = document.querySelector("#url-list");
  const emptyMessage = document.querySelector("#no-urls");
  const count = document.querySelector("#url-count");

  count.textContent = numberFormat.format(urls.length);
  emptyMessage.hidden = urls.length > 0;
  list.hidden = urls.length === 0;

  const items = urls.map((url) => {
    const item = document.createElement("li");
    const text = document.createElement("code");
    text.textContent = url;
    item.append(text);
    return item;
  });

  list.replaceChildren(...items);
}

function renderAnalysis(result) {
  const phishing = result.label === "phishing";
  const probability = Math.max(0, Math.min(1, Number(result.phishing_probability)));
  const percent = Math.round(probability * 1000) / 10;
  const verdict = document.querySelector("#verdict");
  const verdictLabel = document.querySelector("#verdict-label");
  const verdictCopy = document.querySelector("#verdict-copy");
  const probabilityValue = document.querySelector("#probability-value");
  const probabilityTrack = document.querySelector("#probability-track");
  const probabilityFill = document.querySelector("#probability-fill");

  verdict.classList.toggle("is-phishing", phishing);
  verdict.classList.toggle("is-safe", !phishing);
  verdictLabel.textContent = phishing ? "Indikasi phishing" : "Aman menurut model";
  verdictCopy.textContent = phishing
    ? "Model mengklasifikasikan email ini sebagai phishing."
    : "Model mengklasifikasikan email ini sebagai aman. Periksa konteks sebelum membuka tautan.";

  probabilityValue.textContent = percentFormat.format(probability);
  probabilityTrack.setAttribute("aria-valuenow", String(Math.round(percent)));
  probabilityTrack.setAttribute("aria-valuetext", percentFormat.format(probability));
  probabilityFill.style.width = `${percent}%`;

  renderSignals(result.url_signals);
  renderUrls(result.urls);

  emptyReport.hidden = true;
  reportError.hidden = true;
  analysisResult.hidden = false;
  analysisResult.classList.remove("is-entering");
  window.requestAnimationFrame(() => analysisResult.classList.add("is-entering"));
  reportState.textContent = "Selesai";
  resetButton.disabled = false;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  clearMessages();

  const subject = subjectField.value.trim();
  const body = bodyField.value.trim();
  if (!subject && !body) {
    editorError.textContent = "Isi subjek atau isi email terlebih dahulu.";
    editorError.hidden = false;
    subjectField.focus();
    return;
  }

  emptyReport.hidden = true;
  analysisResult.hidden = true;
  reportError.hidden = true;
  reportState.textContent = "Sedang memeriksa";
  setBusy(true);

  try {
    const response = await fetch("/api/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({ subject, body }),
    });
    const result = await response.json().catch(() => ({}));

    if (!response.ok) {
      throw new Error(result.error || "Email belum dapat dianalisis.");
    }

    renderAnalysis(result);
  } catch (error) {
    reportState.textContent = "Pemeriksaan gagal";
    reportError.textContent = error instanceof Error
      ? error.message
      : "Pemeriksaan gagal. Periksa koneksi aplikasi lalu coba lagi.";
    reportError.hidden = false;
    resetButton.disabled = false;
  } finally {
    setBusy(false);
  }
});

document.querySelector("#load-sample").addEventListener("click", () => {
  subjectField.value = sampleSubject;
  bodyField.value = sampleBody;
  handleDraftChange();
  bodyField.focus();
});

resetButton.addEventListener("click", () => {
  form.reset();
  clearMessages();
  analysisResult.hidden = true;
  analysisResult.classList.remove("is-entering");
  emptyReport.hidden = false;
  reportState.textContent = "Menunggu email";
  report.setAttribute("aria-busy", "false");
  document.querySelector("#probability-fill").style.width = "0";
  document.querySelector("#probability-track").setAttribute("aria-valuenow", "0");
  document.querySelector("#probability-track").setAttribute("aria-valuetext", "0%");
  document.querySelector("#probability-value").textContent = "—";
  document.querySelector("#signal-list").replaceChildren();
  document.querySelector("#url-list").replaceChildren();
  document.querySelector("#url-list").hidden = false;
  document.querySelector("#no-urls").hidden = true;
  document.querySelector("#url-count").textContent = "0";
  emptyReportTitle.textContent = "Belum ada hasil.";
  emptyReportCopy.textContent = "Klasifikasi dan sinyal yang terukur akan muncul di sini setelah email dianalisis.";
  updateCharacterCount();
  subjectField.focus();
});

subjectField.addEventListener("input", handleDraftChange);
bodyField.addEventListener("input", handleDraftChange);

updateCharacterCount();
checkModel();
