import os

# 1. Expand Final Grade Calculator
path1 = "tools/final-grade-calculator/index.html"
with open(path1, "r", encoding="utf-8") as f:
    c = f.read()

# I will replace everything after </script> and before </article> with expanded content
old_content1_start = c.find('</script>') + len('</script>')
old_content1_end = c.find('</article>')
old_content1 = c[old_content1_start:old_content1_end]

new_content1 = """
  <p>The end of the semester is stressful enough without having to guess what you need to score on your final exam. Our Final Grade Calculator does the math for you instantly, helping you prioritize your study time for the exams that matter most.</p>
  
  <h2>How to use the Final Grade Calculator</h2>
  <ul>
    <li><strong>Current Grade:</strong> Look at your syllabus or student portal and enter your current overall grade percentage before taking the final exam.</li>
    <li><strong>Desired Grade:</strong> Enter the final percentage you want to achieve in the class (e.g., 90% for an A, 80% for a B, or 70% to pass).</li>
    <li><strong>Final Exam Weight:</strong> Enter what percentage of your total course grade the final exam is worth (usually between 15% and 30%). Check your syllabus for the exact weight.</li>
  </ul>
  
  <h2>Formula Used</h2>
  <p>If you prefer to do the math manually, here is the standard algebraic formula we use to calculate your required final score:</p>
  <p><em>Required Final Score = [Desired Grade - Current Grade × (1 - Final Weight)] / Final Weight</em></p>
  <p>For example, if you have an 85% in the class, want a 90%, and the final is worth 20% (0.20), the math is: [90 - (85 * 0.8)] / 0.20 = [90 - 68] / 0.20 = 22 / 0.20 = 110%. You would need 110% on the final to get an A, which requires extra credit.</p>
  
  <h2>Tips for Finals Week</h2>
  <p>If the calculator tells you that you need over 100%, it might be time to speak to your professor about extra credit opportunities or adjust your expectations. If you only need a very low score to keep your current grade (e.g., 40%), you can afford to allocate more study time to your harder classes where your grade is borderline!</p>

  <h2>Frequently asked questions</h2>
  <h3>What if my final exam is worth points instead of a percentage?</h3>
  <p>If your class uses a points system instead of weighted percentages, you can calculate the final exam weight yourself. Simply divide the total points the final exam is worth by the total points in the entire course. For example, if the final is worth 100 points out of 500 total points for the semester, the final exam weight is 20%.</p>
  
  <h3>Does this calculator work for college and high school?</h3>
  <p>Yes, this calculator works for any grading system that uses percentages. Whether you are in middle school, high school, or a university undergraduate or graduate program, the mathematical formula remains exactly the same.</p>

  <h2>Related tools</h2>
  <h3><a href="/tools/gpa-percentage-converter/">GPA to percentage converter</a></h3>
  <p>Convert your final percentage grade into a standard 4.0 scale GPA.</p>
  <h3><a href="/tools/college-chances-calculator/">College admissions chances predictor</a></h3>
  <p>See how your final grades affect your chances of getting into top colleges.</p>
  <h3><a href="/tools/ap-gpa-calculator/">AP GPA calculator</a></h3>
  <p>Calculate your weighted GPA based on your AP course results.</p>
"""

c = c[:old_content1_start] + new_content1 + c[old_content1_end:]
with open(path1, "w", encoding="utf-8") as f:
    f.write(c)


# 2. Expand College Chances Calculator
path2 = "tools/college-chances-calculator/index.html"
with open(path2, "r", encoding="utf-8") as f:
    c2 = f.read()

old_content2_start = c2.find('</script>') + len('</script>')
old_content2_end = c2.find('</article>')
old_content2 = c2[old_content2_start:old_content2_end]

new_content2 = """
  <p>Figuring out where to apply to college can be overwhelming. The College Admissions Chances Predictor is designed to help you quickly identify whether a university should be considered a Safety, Match, or Reach school based on historical admissions data and your current academic profile.</p>

  <h2>How do admissions chances work?</h2>
  <p>Most college counselors divide your college list into three distinct categories based on your academic profile compared to the school's historical admitted student data:</p>
  <ul>
    <li><strong>Safety Schools:</strong> Your GPA and SAT/ACT scores are well above the 75th percentile for admitted students. The school has a relatively high acceptance rate, making your admission highly likely.</li>
    <li><strong>Match Schools (Target):</strong> Your academic profile falls squarely between the 25th and 75th percentile of admitted students. You have a realistic chance of getting in, but it's not guaranteed.</li>
    <li><strong>Reach Schools:</strong> Your academic profile is below the 25th percentile, OR the school is so hyper-selective (like the Ivy League) that it is a reach for absolutely everyone, regardless of perfect scores.</li>
  </ul>
  
  <h2>Important Limitations & Holistic Admissions</h2>
  <p>This calculator relies entirely on quantitative metrics: GPA and SAT/ACT scores. While these are usually the most critical factors in college admissions, they do not tell the whole story. Holistic admissions processes, especially at top-tier universities, heavily weigh your application essays, letters of recommendation, extracurricular activities, and demonstrated interest. A perfect score does not guarantee admission to Harvard or Stanford, and a lower score doesn't mean an automatic rejection if you have extraordinary extracurriculars.</p>
  
  <h2>Frequently asked questions</h2>
  <h3>What is a "Far Reach" school?</h3>
  <p>A "Far Reach" school is one where your academic profile is significantly below the historical average of admitted students (e.g., applying to Princeton with a 3.2 GPA and an 1100 SAT). While miracles do happen, students in this category usually require a massive "hook" (like being a recruited athlete or a child of a major donor) to gain admission.</p>
  
  <h3>Are Ivy League schools ever considered a "Safety"?</h3>
  <p>No. Universities with acceptance rates below 10% (like Harvard, Yale, Princeton, Stanford, and MIT) are considered "Reach" schools for absolutely every applicant, regardless of whether you have a 4.0 GPA and a 1600 SAT. There are simply too many highly qualified applicants for the limited number of spots.</p>

  <h3>Should I submit my SAT/ACT score if it's test-optional?</h3>
  <p>If your SAT/ACT score places a school in the "Safety" or "Match" category, you should definitely submit it. If your score lowers your prediction to a "Reach", you might want to consider applying test-optional if the university allows it, and rely on your strong GPA instead.</p>

  <h2>Related tools</h2>
  <h3><a href="/tools/sat-score-estimator/">SAT Score Estimator</a></h3>
  <p>Calculate your total SAT score and see its competitiveness band.</p>
  <h3><a href="/tools/act-to-sat-converter/">ACT to SAT Score Converter</a></h3>
  <p>Convert your ACT composite score to an approximate SAT total.</p>
  <h3><a href="/tools/us-college-fit-quiz/">US College Fit Quiz</a></h3>
  <p>Find your best-fit US college type based on size, setting, and culture.</p>
"""

c2 = c2[:old_content2_start] + new_content2 + c2[old_content2_end:]
with open(path2, "w", encoding="utf-8") as f:
    f.write(c2)

print("Expanded content for both tools")
