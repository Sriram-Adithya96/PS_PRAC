const LINEAR_API = "http://127.0.0.1:8000/predict";
const MUSHROOM_API = "http://127.0.0.1:8001/predict";

const mushroomFields = [
  { name: "cap_shape", label: "Cap Shape", options: ["b", "c", "x", "f", "k", "s"] },
  { name: "cap_surface", label: "Cap Surface", options: ["f", "g", "y", "s"] },
  { name: "cap_color", label: "Cap Color", options: ["n", "y", "w", "g", "e", "p", "b", "u", "c", "r"] },
  { name: "bruises", label: "Bruises", options: ["t", "f"] },
  { name: "odor", label: "Odor", options: ["a", "l", "c", "y", "f", "m", "n", "p", "s"] },
  { name: "gill_attachment", label: "Gill Attachment", options: ["a", "d", "f", "n"] },
  { name: "gill_spacing", label: "Gill Spacing", options: ["c", "w", "d"] },
  { name: "gill_size", label: "Gill Size", options: ["b", "n"] },
  { name: "gill_color", label: "Gill Color", options: ["k", "n", "b", "h", "g", "r", "o", "p", "u", "e", "w", "y"] },
  { name: "stalk_shape", label: "Stalk Shape", options: ["e", "t"] },
  { name: "stalk_root", label: "Stalk Root", options: ["b", "c", "u", "e", "z", "r", "?"] },
  { name: "stalk_surface_above_ring", label: "Stalk Surface Above Ring", options: ["f", "y", "k", "s"] },
  { name: "stalk_surface_below_ring", label: "Stalk Surface Below Ring", options: ["f", "y", "k", "s"] },
  { name: "stalk_color_above_ring", label: "Stalk Color Above Ring", options: ["n", "b", "c", "g", "o", "p", "e", "w", "y"] },
  { name: "stalk_color_below_ring", label: "Stalk Color Below Ring", options: ["n", "b", "c", "g", "o", "p", "e", "w", "y"] },
  { name: "veil_color", label: "Veil Color", options: ["n", "o", "w", "y"] },
  { name: "ring_number", label: "Ring Number", options: ["n", "o", "t"] },
  { name: "ring_type", label: "Ring Type", options: ["c", "e", "f", "l", "n", "p", "s", "z"] },
  { name: "spore_print_color", label: "Spore Print Color", options: ["k", "n", "b", "h", "r", "o", "u", "w", "y"] },
  { name: "population", label: "Population", options: ["a", "c", "n", "s", "v", "y"] },
  { name: "habitat", label: "Habitat", options: ["g", "l", "m", "p", "u", "w", "d"] }
];

const houseNumericFields = ["area", "bedrooms", "bathrooms", "stories", "parking"];
const modelTabs = document.querySelectorAll(".model-card");
const housePanel = document.querySelector("#house-panel");
const mushroomPanel = document.querySelector("#mushroom-panel");
const mushroomFieldsContainer = document.querySelector("#mushroom-fields");

function createMushroomFields() {
  for (const field of mushroomFields) {
    const label = document.createElement("label");
    label.className = "field";

    const title = document.createElement("span");
    title.textContent = field.label;

    const select = document.createElement("select");
    select.name = field.name;
    select.required = true;
    select.setAttribute("aria-label", field.label);

    const placeholder = document.createElement("option");
    placeholder.value = "";
    placeholder.textContent = "Select a code";
    placeholder.disabled = true;
    placeholder.selected = true;
    select.append(placeholder);

    for (const code of field.options) {
      const option = document.createElement("option");
      option.value = code;
      option.textContent = code;
      select.append(option);
    }

    label.append(title, select);
    mushroomFieldsContainer.append(label);
  }
}

function showResult(container, { label, value, detail, isError = false }) {
  container.replaceChildren();
  container.dataset.state = isError ? "error" : "success";

  const resultLabel = document.createElement("span");
  resultLabel.className = "result-label";
  resultLabel.textContent = label;
  container.append(resultLabel);

  const resultValue = document.createElement("strong");
  resultValue.className = "result-value";
  resultValue.textContent = value;
  container.append(resultValue);

  if (detail) {
    const resultDetail = document.createElement("span");
    resultDetail.className = "result-detail";
    resultDetail.textContent = detail;
    container.append(resultDetail);
  }

  container.hidden = false;
}

async function postPrediction(url, payload) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    let detail = "";
    try {
      const errorBody = await response.json();
      if (typeof errorBody.detail === "string") {
        detail = `: ${errorBody.detail}`;
      }
    } catch {
      // Use the HTTP status when the server does not return a JSON error body.
    }
    throw new Error(`The prediction service returned HTTP ${response.status}${detail}`);
  }

  return response.json();
}

function setSubmitting(form, isSubmitting, buttonText) {
  const button = form.querySelector('button[type="submit"]');
  button.disabled = isSubmitting;
  button.querySelector("span").textContent = isSubmitting ? "Predicting…" : buttonText;
}

createMushroomFields();

for (const tab of modelTabs) {
  tab.addEventListener("click", () => {
    const showHouse = tab.dataset.model === "house";
    housePanel.hidden = !showHouse;
    mushroomPanel.hidden = showHouse;

    for (const modelTab of modelTabs) {
      const selected = modelTab === tab;
      modelTab.classList.toggle("is-selected", selected);
      modelTab.setAttribute("aria-pressed", String(selected));
    }
  });
}

document.querySelector("#house-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const form = event.currentTarget;
  const resultBox = document.querySelector("#house-result");
  if (!form.reportValidity()) {
    return;
  }

  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());
  for (const field of houseNumericFields) {
    payload[field] = Number(payload[field]);
    if (!Number.isFinite(payload[field])) {
      showResult(resultBox, {
        label: "Input error",
        value: "Please enter valid numeric values for the house details.",
        isError: true
      });
      return;
    }
  }

  setSubmitting(form, true, "Predict House Price");
  resultBox.hidden = true;
  try {
    const data = await postPrediction(LINEAR_API, payload);
    if (typeof data.predicted_price !== "number" || !Number.isFinite(data.predicted_price)) {
      throw new Error("The prediction service returned an invalid predicted_price value.");
    }

    const formattedPrice = new Intl.NumberFormat("en-IN", {
      style: "currency",
      currency: "INR",
      maximumFractionDigits: 2
    }).format(data.predicted_price);
    showResult(resultBox, {
      label: "Predicted house price",
      value: formattedPrice,
      detail: "Estimate returned by the Linear Regression model."
    });
  } catch (error) {
    showResult(resultBox, {
      label: "Prediction unavailable",
      value: error instanceof Error ? error.message : "Unable to reach the house price service.",
      detail: "Check that the Linear Regression API is running at 127.0.0.1:8000.",
      isError: true
    });
  } finally {
    setSubmitting(form, false, "Predict House Price");
  }
});

document.querySelector("#mushroom-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const form = event.currentTarget;
  const resultBox = document.querySelector("#mushroom-result");
  if (!form.reportValidity()) {
    return;
  }

  const payload = Object.fromEntries(new FormData(form).entries());
  setSubmitting(form, true, "Predict Mushroom");
  resultBox.hidden = true;
  try {
    const data = await postPrediction(MUSHROOM_API, payload);
    const expectedResult = data.prediction === "e"
      ? "Edible"
      : data.prediction === "p"
        ? "Poisonous"
        : null;

    if (!expectedResult || data.result !== expectedResult) {
      throw new Error("The prediction service returned an invalid mushroom classification.");
    }

    showResult(resultBox, {
      label: "Mushroom classification",
      value: data.result,
      detail: `Model prediction: ${data.prediction}`
    });
  } catch (error) {
    showResult(resultBox, {
      label: "Prediction unavailable",
      value: error instanceof Error ? error.message : "Unable to reach the mushroom classification service.",
      detail: "Check that the Decision Tree API is running at 127.0.0.1:8001.",
      isError: true
    });
  } finally {
    setSubmitting(form, false, "Predict Mushroom");
  }
});
