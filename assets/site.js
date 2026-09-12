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
    if (/ib-total/.test(slug)) return "ib";
    if (/ucas-tariff/.test(slug)) return "ucas";
    if (/quiz|checklist|readiness|eligibility|fit/.test(slug)) return "quiz";
    if (/timeline|planner/.test(slug)) return "quiz";
    if (/loan/.test(slug)) return "loan";
    if (/comparison|vs/.test(slug)) return "compare";
    if (/cost|budget|fees|living|dorm|public-school/.test(slug)) return "cost";
    if (/converter|percentage/.test(slug)) return "converter";
    return "score";
  }

  function getIELTSFromPTE(pte) {
    if (pte >= 90) return 9.0;
    if (pte >= 86) return 8.5;
    if (pte >= 79) return 8.0;
    if (pte >= 71) return 7.5;
    if (pte >= 63) return 7.0;
    if (pte >= 58) return 6.5;
    if (pte >= 50) return 6.0;
    if (pte >= 43) return 5.5;
    if (pte >= 36) return 5.0;
    if (pte >= 30) return 4.5;
    return "< 4.5";
  }

  function getIELTSFromDET(det) {
    if (det >= 155) return 9.0;
    if (det >= 145) return 8.5;
    if (det >= 135) return 8.0;
    if (det >= 125) return 7.5;
    if (det >= 115) return 7.0;
    if (det >= 105) return 6.5;
    if (det >= 95) return 6.0;
    if (det >= 85) return 5.5;
    if (det >= 75) return 5.0;
    if (det >= 65) return 4.5;
    return "< 4.5";
  }

  function getTOEFLFromIELTS(ielts) {
    if (ielts >= 9.0) return "118-120";
    if (ielts >= 8.5) return "115-117";
    if (ielts >= 8.0) return "110-114";
    if (ielts >= 7.5) return "102-109";
    if (ielts >= 7.0) return "94-101";
    if (ielts >= 6.5) return "79-93";
    if (ielts >= 6.0) return "60-78";
    if (ielts >= 5.5) return "46-59";
    if (ielts >= 5.0) return "35-45";
    if (ielts >= 4.5) return "32-34";
    return "0-31";
  }

  function renderTool(panel) {
    if (panel.hasAttribute('data-custom')) return;

    var slug = panel.getAttribute("data-tool") || "";
    var runtime = panel.querySelector(".tool-runtime");
    var mode = toolMode(slug);

    if (mode === "quiz") {
      var labels = ["I verified the institution or programme in an official source.", "I checked the full cost, not only advertised tuition.", "I reviewed entry requirements for my qualification.", "I compared support, location and learning format.", "I saved source links and the date checked."];
      runtime.innerHTML = '<div class="checklist-tool">' + labels.map(function (label) { return '<label><input type="checkbox"><span>' + label + '</span></label>'; }).join("") + '</div><div class="tool-result" role="status">0/5 research checks complete</div>';
      runtime.addEventListener("change", function () { runtime.querySelector(".tool-result").textContent = runtime.querySelectorAll('input:checked').length + "/5 research checks complete"; });
      return;
    }

    if (mode === "ib") {
       var ibLabels = ["Subject 1 (0-7)", "Subject 2 (0-7)", "Subject 3 (0-7)", "Subject 4 (0-7)", "Subject 5 (0-7)", "Subject 6 (0-7)", "Core Points (0-3)"];
       runtime.innerHTML = '<div class="tool-fields">' + ibLabels.map(function(l) { return '<label><span>'+l+'</span><input type="number" min="0" step="1"></label>'; }).join("") + '</div><button class="button button-primary" type="button">Calculate IB Total</button><div class="tool-result" role="status" hidden></div>';

       runtime.querySelector("button").addEventListener("click", function() {
           var inputs = Array.from(runtime.querySelectorAll("input"));
           var vals = inputs.map(function(i) { return parseInt(i.value) || 0; });
           var error = false;
           var subjTotal = 0;
           for(var i=0; i<6; i++) {
               if (vals[i] < 0 || vals[i] > 7) error = true;
               subjTotal += vals[i];
           }
           if (vals[6] < 0 || vals[6] > 3) error = true;

           var result = runtime.querySelector(".tool-result");
           if (error) {
               result.textContent = "Error: Please enter valid scores (0-7 for subjects, 0-3 for core points).";
           } else {
               var total = subjTotal + vals[6];
               result.innerHTML = "Subject Total: " + subjTotal + " | Core Points: " + vals[6] + "<br><strong>Final IB Total: " + total + " / 45</strong><br><small>This calculator estimates the IB Diploma total from the entered subject scores and core points. (Does not convert IB to GPA).</small>";
           }
           result.hidden = false;
       });
       return;
    }

    if (mode === "ucas") {
       var ucasOptions = [
           {label: "-- Select Qualification & Grade --", val: 0},
           {label: "A-Level: A*", val: 56}, {label: "A-Level: A", val: 48}, {label: "A-Level: B", val: 40}, {label: "A-Level: C", val: 32}, {label: "A-Level: D", val: 24}, {label: "A-Level: E", val: 16},
           {label: "AS-Level: A", val: 20}, {label: "AS-Level: B", val: 16}, {label: "AS-Level: C", val: 12}, {label: "AS-Level: D", val: 10}, {label: "AS-Level: E", val: 6},
           {label: "BTEC Ext Dip: D*D*D*", val: 168}, {label: "BTEC Ext Dip: D*D*D", val: 160}, {label: "BTEC Ext Dip: DDD", val: 144}, {label: "BTEC Ext Dip: DDM", val: 128}, {label: "BTEC Ext Dip: DMM", val: 112}, {label: "BTEC Ext Dip: MMM", val: 96}, {label: "BTEC Ext Dip: MMP", val: 80}, {label: "BTEC Ext Dip: MPP", val: 64}, {label: "BTEC Ext Dip: PPP", val: 48},
           {label: "Scottish Higher: A", val: 33}, {label: "Scottish Higher: B", val: 27}, {label: "Scottish Higher: C", val: 21}, {label: "Scottish Higher: D", val: 15}
       ];
       var optHTML = ucasOptions.map(function(o) { return '<option value="'+o.val+'">'+o.label+(o.val>0 ? ' ('+o.val+' pts)' : '')+'</option>'; }).join("");

       var fields = "";
       for(var i=1; i<=5; i++) {
           fields += '<label><span>Qualification '+i+'</span><select class="ucas-select">'+optHTML+'</select></label>';
       }

       runtime.innerHTML = '<div class="tool-fields">' + fields + '</div><button class="button button-primary" type="button">Calculate Tariff</button><div class="tool-result" role="status" hidden></div>';

       runtime.querySelector("button").addEventListener("click", function() {
           var selects = Array.from(runtime.querySelectorAll(".ucas-select"));
           var total = 0;
           var breakdown = [];
           selects.forEach(function(sel) {
               var val = parseInt(sel.value) || 0;
               if (val > 0) {
                   var text = sel.options[sel.selectedIndex].text;
                   breakdown.push(text);
                   total += val;
               }
           });

           var result = runtime.querySelector(".tool-result");
           if (breakdown.length === 0) {
               result.textContent = "Please select at least one qualification.";
           } else {
               result.innerHTML = "<strong>Selected:</strong><br>" + breakdown.join("<br>") + "<br><br><strong>Total UCAS Tariff Points: " + total + "</strong><br><small>Note: Universities may set their own entry requirements. Tariff points do not guarantee admission.</small><br><br><small><strong>Methodology:</strong> Tariff values are based on current UCAS Tariff tables (Selected Common UK Qualifications). For qualifications not listed here, use the <a href=\"https://www.ucas.com/applying/before-you-apply/what-and-where-to-study/entry-requirements/calculate-your-ucas-tariff-points\" target=\"_blank\" rel=\"noopener\">official UCAS Tariff calculator</a>.</small>";
           }
           result.hidden = false;
       });
       return;
    }

    var labels = [];
    if (mode === "loan") labels = ["Loan principal", "Annual interest rate (%)", "Loan term in years"];
    else if (mode === "compare") labels = ["Scenario A: Tuition/Rent", "Scenario A: Food/Living", "Scenario B: Tuition/Rent", "Scenario B: Food/Living"];
    else if (mode === "cost") labels = ["Annual tuition", "Monthly living cost", "Annual fees & insurance", "Annual travel & extras"];
    else if (mode === "converter") labels = ["Value to convert"];
    else if (/weighted-gpa|ap-gpa/.test(slug)) labels = ["Unweighted GPA", "AP/IB courses", "Honors courses", "Total courses"];
    else labels = ["Academic score", "Course rigor", "Relevant test score", "Other factor"];

    runtime.innerHTML = '<div class="tool-fields">' + labels.map(function (label) { return '<label><span>' + label + '</span><input type="number" min="0" step="0.01" inputmode="decimal"></label>'; }).join("") + '</div><button class="button button-primary" type="button">Calculate estimate</button><div class="tool-result" role="status" hidden></div>';

    runtime.querySelector("button").addEventListener("click", function () {
      var values = Array.from(runtime.querySelectorAll("input")).map(function (input) { return Number(input.value) || 0; });
      var text = "";

      if (mode === "loan") {
        var P = values[0];
        var rate = values[1];
        var years = values[2];
        if (P <= 0 || years <= 0) {
            text = "Please enter a valid principal and term greater than 0.";
        } else {
            var n = years * 12;
            var r = rate / 100 / 12;
            var payment = 0;
            if (r === 0) payment = P / n;
            else payment = P * (r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
            var totalRepayment = payment * n;
            var totalInterest = totalRepayment - P;
            text = "Planning estimate: $" + payment.toFixed(2) + " / month (Total Repayment: $" + totalRepayment.toFixed(2) + ", Interest: $" + totalInterest.toFixed(2) + "). Actual repayment depends on the loan agreement.";
        }
      }
      else if (mode === "compare") {
        var totalA = values[0] + values[1];
        var totalB = values[2] + values[3];
        var diff = Math.abs(totalA - totalB);
        var moreExp = totalA > totalB ? "Scenario A" : (totalB > totalA ? "Scenario B" : "Neither");
        text = "Scenario A Total: " + totalA.toLocaleString() + " | Scenario B Total: " + totalB.toLocaleString() + ". Difference: " + diff.toLocaleString() + " (" + moreExp + " is more expensive).";
      }
      else if (mode === "cost") {
        text = "Estimated annual total: " + Math.round(values[0] + values[1] * 12 + values[2] + values[3]).toLocaleString();
      }
      else if (mode === "converter") {
        if (/pte-ielts/.test(slug)) {
            text = "Concordance estimate: IELTS " + getIELTSFromPTE(values[0]) + " (Score equivalencies are approximate concordance estimates, not universal conversions).";
        } else if (/duolingo-ielts/.test(slug)) {
            text = "Concordance estimate: IELTS " + getIELTSFromDET(values[0]) + " (Score equivalencies are approximate concordance estimates, not universal conversions).";
        } else if (/ielts-toefl/.test(slug)) {
            text = "Concordance estimate: LEGACY TOEFL iBT " + getTOEFLFromIELTS(values[0]) + " (Approximate concordance estimate. Note: TOEFL introduced a new 1-6 scale from Jan 2026, check with your institution).";
        } else if (/percentage/.test(slug)) {
            var converted = Math.min(100, values[0] <= 10 ? values[0] * 9.5 : values[0] * 25);
            text = "Planning estimate: " + converted.toFixed(1);
        } else if (/act-to-sat/.test(slug)) {
            var converted = Math.min(1600, Math.max(400, 400 + values[0] * 33.3));
            text = "Planning estimate: " + converted.toFixed(1);
        } else {
            text = "Planning estimate: " + (values[0] * 1.1).toFixed(1);
        }
      } else if (/weighted-gpa|ap-gpa/.test(slug)) {
        text = "Estimated weighted GPA: " + Math.min(5, values[3] > 0 ? values[0] + (values[1] + values[2] * .5) / values[3] : values[0]).toFixed(2);
      } else {
        var entered = values.filter(function (value) { return value > 0; });
        text = "Planning estimate: " + (entered.length ? entered.reduce(function (sum, value) { return sum + value; }, 0) / entered.length : 0).toFixed(1);
      }
      var result = runtime.querySelector(".tool-result"); result.textContent = text; result.hidden = false;
    });
  }

  document.querySelectorAll("[data-tool]").forEach(renderTool);
})();
