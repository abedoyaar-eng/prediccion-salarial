const API_BASE = "http://127.0.0.1:5000";

let JOBS_JSON = [];
let JOBS_REG = [];

async function loadMetadata() {
  try {
    const r = await fetch(`${API_BASE}/metadata`);
    const j = await r.json();
    JOBS_JSON = j.job_titles_json;
    JOBS_REG = j.job_titles_reg;
    loadJobTitles(JOBS_REG);
  } catch (err) {
    document.getElementById("jobTitle").innerHTML =
      "<option>Error cargando</option>";
  }
}

function loadJobTitles(list) {
  const sel = document.getElementById("jobTitle");
  sel.innerHTML = "";
  list.forEach(t => {
    const opt = document.createElement("option");
    opt.value = t;
    opt.textContent = t;
    sel.appendChild(opt);
  });
}

document.querySelectorAll("input[name='modelRadio']").forEach(r => {
  r.addEventListener("change", () => {
    const model = getSelectedModel();
    if (model === "regression") loadJobTitles(JOBS_REG);
    else loadJobTitles(JOBS_JSON);
  });
});

function getSelectedModel() {
  const radios = document.getElementsByName("modelRadio");
  for (const r of radios) if (r.checked) return r.value;
  return "regression";
}

function collectFeatures() {
  return {
    Age: Number(document.getElementById("age").value),
    Gender: Number(document.getElementById("gender").value),
    "Education Level": Number(document.getElementById("education").value),
    "Job Title": document.getElementById("jobTitle").value,
    "Years of Experience": Number(document.getElementById("years").value)
  };
}

async function sendPrediction() {
  const model = getSelectedModel();
  const features = collectFeatures();
  const resultBody = document.getElementById("resultBody");
  const resultCard = document.getElementById("resultCard");

  resultBody.innerHTML = "Procesando...";
  resultCard.classList.remove("d-none");

  try {
    const r = await fetch(`${API_BASE}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model, features })
    });

    const j = await r.json();

    if (r.ok) {
      if (j.model === "regression") {
        resultBody.innerHTML =
          `<p><strong>Salario estimado:</strong> $${j.predicted_salary.toFixed(2)}</p>
           <p><strong>Rango estimado:</strong> ${j.predicted_category}</p>`;
      } else {
        resultBody.innerHTML =
          `<p><strong>Rango predicho:</strong> ${j.label}</p>`;
      }
    } else {
      resultBody.innerHTML = `<div class="text-danger">Error: ${j.error}</div>`;
    }
  } catch {
    resultBody.innerHTML =
      `<div class="text-danger">Error de conexión al backend.</div>`;
  }
}

function resetForm() {
  document.getElementById("predictForm").reset();
  document.getElementById("resultCard").classList.add("d-none");
}

loadMetadata();
