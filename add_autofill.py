import os

path = "tools/wam-calculator/index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Add a datalist right after <div id="subjects_container">
datalist_html = """
    <datalist id="common-subjects">
      <option value="FIT1045 - Algorithms and programming in Python" data-cp="6">
      <option value="FIT1047 - Introduction to computer systems, networks and security" data-cp="6">
      <option value="FIT1049 - IT professional practice" data-cp="6">
      <option value="FIT1051 - Programming fundamentals in java" data-cp="6">
      <option value="FIT2001 - Systems development" data-cp="6">
      <option value="FIT2004 - Algorithms and data structures" data-cp="6">
      <option value="FIT2014 - Theory of computation" data-cp="6">
      <option value="FIT2099 - Object-oriented design and implementation" data-cp="6">
      <option value="FIT3155 - Advanced data structures and algorithms" data-cp="6">
      <option value="MAT1830 - Discrete mathematics for computer science" data-cp="6">
      <option value="MAT1841 - Continuous mathematics for computer science" data-cp="6">
      <option value="ENG1001 - Engineering design: lighter, faster, stronger" data-cp="6">
      <option value="ENG1002 - Engineering design: cleaner, safer, smarter" data-cp="6">
      <option value="ENG1003 - Engineering mobile apps" data-cp="6">
      <option value="ENG1011 - Engineering methods" data-cp="6">
      <option value="ENG1012 - Engineering design" data-cp="6">
      <option value="ENG1013 - Engineering smart systems" data-cp="6">
      <option value="ENG1014 - Engineering numerical analysis" data-cp="6">
      <option value="ACC1100 - Introduction to financial accounting" data-cp="6">
      <option value="ACC1200 - Accounting for managers" data-cp="6">
      <option value="BFC1001 - Foundations of finance" data-cp="6">
      <option value="BTC1110 - Commercial law" data-cp="6">
      <option value="ECC1000 - Principles of microeconomics" data-cp="6">
      <option value="ECC1100 - Principles of macroeconomics" data-cp="6">
      <option value="ETC1000 - Business and economic statistics" data-cp="6">
      <option value="MGC1010 - Introduction to management" data-cp="6">
      <option value="MKC1200 - Principles of marketing" data-cp="6">
      <option value="LAW1111 - Foundations of law" data-cp="6">
      <option value="LAW1112 - Public law and statutory interpretation" data-cp="6">
      <option value="LAW1114 - Criminal law 1" data-cp="6">
      <option value="BMS1011 - Biomedical chemistry" data-cp="6">
      <option value="BMS1021 - Cells, tissues and organisms" data-cp="6">
      <option value="BMS1031 - Medical biophysics" data-cp="6">
      <option value="MED1011 - Medicine 1" data-cp="12">
      <option value="MED1022 - Medicine 2" data-cp="12">
      <option value="MED2031 - Medicine 3" data-cp="12">
      <option value="MED2042 - Medicine 4" data-cp="12">
    </datalist>
"""

# Link existing inputs to the datalist
c = c.replace('<div id="subjects_container">', '<div id="subjects_container">\n' + datalist_html)
c = c.replace('class="subj-name"', 'class="subj-name" list="common-subjects"')

# Also add JS to auto-save to localstorage, AND auto-calculate when mark is entered.
js_additions = """
    // Function to calculate and save
    function calculateWAM() {
      var rows = document.querySelectorAll(".subject-row");
      var totalWeightedMarks = 0;
      var totalCredits = 0;
      var subjectsData = [];
      
      rows.forEach(function(row) {
        var name = row.querySelector(".subj-name").value;
        var mark = parseFloat(row.querySelector(".subj-mark").value);
        var credit = parseFloat(row.querySelector(".subj-credit").value);
        
        subjectsData.push({ name: name, mark: isNaN(mark) ? "" : mark, credit: isNaN(credit) ? 6 : credit });
        
        if (!isNaN(mark) && !isNaN(credit)) {
          totalWeightedMarks += (mark * credit);
          totalCredits += credit;
        }
      });
      
      // Auto-save to local storage
      localStorage.setItem("wamSubjects", JSON.stringify(subjectsData));
      
      var resultBox = document.getElementById("result_box");
      if (totalCredits === 0) {
        resultBox.innerHTML = "<p>Enter your marks to see your WAM automatically.</p>";
        resultBox.style.borderColor = "rgba(255,255,255,0.2)";
        resultBox.style.color = "white";
        resultBox.style.background = "rgba(255,255,255,0.08)";
      } else {
        var wam = (totalWeightedMarks / totalCredits).toFixed(3);
        var gradeDesc = "";
        if (wam >= 80) gradeDesc = "High Distinction (HD)";
        else if (wam >= 70) gradeDesc = "Distinction (D)";
        else if (wam >= 60) gradeDesc = "Credit (C)";
        else if (wam >= 50) gradeDesc = "Pass (P)";
        else gradeDesc = "Fail (N)";
        
        resultBox.innerHTML = "<h3>Your WAM is " + wam + "</h3><p>Equivalent to a <strong>" + gradeDesc + "</strong></p>";
        resultBox.style.borderColor = "rgba(40,167,69,0.3)";
        resultBox.style.color = "#8de49f";
        resultBox.style.background = "rgba(40,167,69,0.15)";
      }
      resultBox.hidden = false;
    }

    // Auto-calculate on input change
    document.getElementById("subjects_container").addEventListener("input", function(e) {
       // If they picked a subject from datalist that has 12 credits, auto-fill it
       if (e.target.classList.contains("subj-name")) {
         var val = e.target.value;
         var option = document.querySelector('#common-subjects option[value="' + val + '"]');
         if (option) {
            var cp = option.getAttribute("data-cp");
            if (cp) {
               e.target.closest(".subject-row").querySelector(".subj-credit").value = cp;
            }
         }
       }
       calculateWAM();
    });

    // Load from local storage on init
    window.addEventListener("DOMContentLoaded", function() {
       var saved = localStorage.getItem("wamSubjects");
       if (saved) {
         try {
           var data = JSON.parse(saved);
           if (data.length > 0) {
             var container = document.getElementById("subjects_container");
             // Keep the datalist but clear rows
             var datalist = container.querySelector("datalist");
             container.innerHTML = "";
             container.appendChild(datalist);
             
             data.forEach(function(item) {
               var row = document.createElement("div");
               row.className = "subject-row";
               row.innerHTML = '<div><label style="font-size:12px; color:#c9d5e4; margin-bottom:5px; display:block;">Subject Name</label><input type="text" placeholder="e.g. FIT1045" class="subj-name" list="common-subjects" value="' + (item.name || '') + '"></div>' +
                               '<div><label style="font-size:12px; color:#c9d5e4; margin-bottom:5px; display:block;">Mark (0-100)</label><input type="number" placeholder="e.g. 85" min="0" max="100" class="subj-mark" value="' + (item.mark !== "" ? item.mark : '') + '"></div>' +
                               '<div><label style="font-size:12px; color:#c9d5e4; margin-bottom:5px; display:block;">Credit Pts</label><input type="number" placeholder="e.g. 6" min="1" class="subj-credit" value="' + (item.credit || 6) + '"></div>' +
                               '<button class="remove-btn" type="button" title="Remove row">X</button>';
               container.appendChild(row);
             });
           }
         } catch(e) {}
       }
       calculateWAM();
    });
"""

# Replace the existing click listener for calc_btn with the new calculateWAM() call.
old_calc_logic_start = c.find('document.getElementById("calc_btn").addEventListener("click", function() {')
old_calc_logic_end = c.find('});\n  </script>', old_calc_logic_start) + 3

c = c[:old_calc_logic_start] + "document.getElementById('calc_btn').addEventListener('click', calculateWAM);\n" + js_additions + c[old_calc_logic_end:]

# Update the add_btn innerHTML to include list="common-subjects"
c = c.replace('class="subj-name"></div>', 'class="subj-name" list="common-subjects"></div>')

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Added autofill datalist, localstorage auto-save, and live auto-calculation!")
