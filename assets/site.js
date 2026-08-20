(function () {
  var searchIndex = null;
  function setupSearch(root) {
    var input = root.querySelector("input");
    var results = root.querySelector(".search-results");
    if (!input || !results) return;
    input.addEventListener("input", async function () {
      var query = input.value.trim().toLowerCase();
      if (!query) { results.hidden = true; results.innerHTML = ""; return; }
      if (!searchIndex) {
        try { searchIndex = await fetch("/assets/search-index.json").then(function (response) { return response.json(); }); }
        catch (error) { searchIndex = []; }
      }
      var terms = query.split(/\s+/);
      var matches = searchIndex.filter(function (item) {
        var haystack = (item.title + " " + item.type).toLowerCase();
        return terms.every(function (term) { return haystack.indexOf(term) >= 0; });
      }).slice(0, root.classList.contains("search-box-compact") ? 5 : 8);
      results.innerHTML = matches.length
        ? matches.map(function (item) { return '<a href="' + item.path + '"><span>' + escapeHtml(item.title) + '</span><small>' + escapeHtml(item.type) + '</small></a>'; }).join("")
        : "<p>No exact match. Try a country, institution or subject.</p>";
      results.hidden = false;
    });
  }
  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (character) { return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[character]; });
  }
  document.querySelectorAll("[data-search]").forEach(setupSearch);

  function toolMode(slug) {
    if (/quiz|checklist|readiness|eligibility|fit/.test(slug)) return "quiz";
    if (/timeline|planner/.test(slug)) return "quiz";
    if (/cost|budget|loan|fees|living|dorm|public-school/.test(slug)) return "cost";
    if (/converter|percentage|tariff/.test(slug)) return "converter";
    return "score";
  }
  function renderTool(panel) {
    var slug = panel.getAttribute("data-tool") || "";
    var runtime = panel.querySelector(".tool-runtime");
    var mode = toolMode(slug);
    if (mode === "quiz") {
      var labels = ["I verified the institution or programme in an official source.", "I checked the full cost, not only advertised tuition.", "I reviewed entry requirements for my qualification.", "I compared support, location and learning format.", "I saved source links and the date checked."];
      runtime.innerHTML = '<div class="checklist-tool">' + labels.map(function (label) { return '<label><input type="checkbox"><span>' + label + '</span></label>'; }).join("") + '</div><div class="tool-result" role="status">0/5 research checks complete</div>';
      runtime.addEventListener("change", function () { runtime.querySelector(".tool-result").textContent = runtime.querySelectorAll('input:checked').length + "/5 research checks complete"; });
      return;
    }
    var labels = mode === "cost" ? ["Annual tuition", "Monthly living cost", "Annual fees & insurance", "Annual travel & extras"] : mode === "converter" ? ["Value to convert"] : /weighted-gpa/.test(slug) ? ["Unweighted GPA", "AP/IB courses", "Honors courses", "Total courses"] : ["Academic score", "Course rigor", "Relevant test score", "Other factor"];
    runtime.innerHTML = '<div class="tool-fields">' + labels.map(function (label) { return '<label><span>' + label + '</span><input type="number" min="0" step="0.01" inputmode="decimal"></label>'; }).join("") + '</div><button class="button button-primary" type="button">Calculate estimate</button><div class="tool-result" role="status" hidden></div>';
    runtime.querySelector("button").addEventListener("click", function () {
      var values = Array.from(runtime.querySelectorAll("input")).map(function (input) { return Number(input.value) || 0; });
      var text = "";
      if (mode === "cost") text = "Estimated annual total: " + Math.round(values[0] + values[1] * 12 + values[2] + values[3]).toLocaleString();
      else if (mode === "converter") {
        var converted = /percentage/.test(slug) ? Math.min(100, values[0] <= 10 ? values[0] * 9.5 : values[0] * 25) : /act-to-sat/.test(slug) ? Math.min(1600, Math.max(400, 400 + values[0] * 33.3)) : values[0] * 1.1;
        text = "Planning estimate: " + converted.toFixed(1);
      } else if (/weighted-gpa/.test(slug)) text = "Estimated weighted GPA: " + Math.min(5, values[3] > 0 ? values[0] + (values[1] + values[2] * .5) / values[3] : values[0]).toFixed(2);
      else { var entered = values.filter(function (value) { return value > 0; }); text = "Planning estimate: " + (entered.length ? entered.reduce(function (sum, value) { return sum + value; }, 0) / entered.length : 0).toFixed(1); }
      var result = runtime.querySelector(".tool-result"); result.textContent = text; result.hidden = false;
    });
  }
  document.querySelectorAll("[data-tool]").forEach(renderTool);
})();
