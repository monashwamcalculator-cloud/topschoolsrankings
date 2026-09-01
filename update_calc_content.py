import os
import re

tools = {
    "college-attendance-safe-bunk-calculator": """
  <div class="rich-article-content" style="margin-top: 40px;">
    <p>College life is a delicate balance between academics and extracurriculars. Whether you are planning a weekend trip, fighting off a fever, or just need a mental health day, knowing exactly how many classes you can afford to miss without dropping below the mandatory 75% or 80% mark is crucial.</p>
    <p>Our <strong>Ultimate Attendance & Safe Bunk Calculator</strong> does the math for you. It tells you your current standing, how many more classes you can safely skip (bunk), or exactly how many consecutive classes you must attend to recover from an attendance shortage.</p>

    <h2>How to Use the Safe Bunk Calculator</h2>
    <ul>
      <li><strong>Current Attendance (%):</strong> Check your student portal (e.g., ERP, TCS iON, or university app) and enter your current attendance percentage.</li>
      <li><strong>Total Classes Conducted So Far:</strong> Enter the number of lectures that have happened up to today.</li>
      <li><strong>Target Attendance (%):</strong> Enter your college's minimum requirement. For most Indian engineering and medical colleges, this is 75%, but some strict universities require 80% or 85%.</li>
    </ul>

    <h2>The Math Behind Attendance Calculation</h2>
    <p>If you want to manually calculate your attendance or understand how the algorithm works, here are the core formulas:</p>
    
    <h3>Formula for Classes Attended</h3>
    <p><em>Classes Attended = (Current Attendance % / 100) × Total Classes Conducted</em></p>

    <h3>Formula for Safe Bunks</h3>
    <p>If your attendance is above the target, you can afford to miss upcoming classes. The formula to find the maximum allowed absences is:</p>
    <p><em>Safe Bunks = (Classes Attended / (Target % / 100)) - Total Classes Conducted</em></p>
    <p>For example: If you have attended 40 out of 50 classes (80%), and your target is 75%, you can safely miss 3 upcoming classes. (40 / 0.75) - 50 = 53.33 - 50 = 3 classes.</p>

    <h3>Formula for Attendance Recovery</h3>
    <p>If you are currently facing an attendance shortage (e.g., 65%), you must attend the next <em>N</em> consecutive classes without missing a single one. The formula is:</p>
    <p><em>Required Classes = [(Target % / 100) × Total Classes - Classes Attended] / [1 - (Target % / 100)]</em></p>

    <h2>Frequently Asked Questions</h2>
    <h3>Does missing a 2-hour lab count as one or two classes?</h3>
    <p>This entirely depends on your university's ERP system. In most universities, a 2-hour lab is logged as 2 separate periods of attendance. If you miss a lab, you are technically bunking 2 classes. Always verify with your professor.</p>

    <h3>What happens if I fall below 75% attendance?</h3>
    <p>Falling below the mandatory limit can lead to severe academic consequences. You may face a <em>"debarred"</em> status, meaning you will not be allowed to sit for your final end-semester examinations. In some cases, medical certificates can grant you a 10% relaxation (bringing the requirement down to 65%), but this is subject to HOD approval.</p>

    <h2>Related Tools</h2>
    <h3><a href="/tools/exam-passing-internal-marks-calculator/">Exam Passing & Internal Marks Calculator</a></h3>
    <p>Find out exactly how many marks you need in your final exam to pass.</p>
    <h3><a href="/tools/cgpa-recovery-placement-target-calculator/">CGPA Recovery & Placement Calculator</a></h3>
    <p>See what GPA you need in your remaining semesters to hit your placement target.</p>
  </div>
""",
    "cgpa-recovery-placement-target-calculator": """
  <div class="rich-article-content" style="margin-top: 40px;">
    <p>Are you worried about campus placements? Most top-tier companies (especially Day 0 and Day 1 recruiters) set strict CGPA cutoffs—usually 7.5, 8.0, or even 8.5. If your current CGPA has dipped due to a tough semester, you need a precise roadmap to bounce back.</p>
    <p>Our <strong>CGPA Recovery & Placement Target Calculator</strong> acts as your academic GPS. It analyzes the credits you've completed and the credits you have left, telling you the exact Semester GPA (SGPA) you need to average from now until graduation to hit your dream target.</p>

    <h2>How to Use the CGPA Recovery Calculator</h2>
    <ul>
      <li><strong>Current CGPA:</strong> Look at your latest transcript and enter your current Cumulative Grade Point Average.</li>
      <li><strong>Credits Completed:</strong> Add up the credits of all the subjects you have successfully passed so far.</li>
      <li><strong>Target CGPA for Placements:</strong> Enter the cutoff for your dream company (e.g., 8.0 for top tech firms).</li>
      <li><strong>Credits Remaining:</strong> Enter the sum of all credits for your upcoming, incomplete semesters. (If you are in 5th semester of a 160-credit degree and have completed 80 credits, your remaining credits are 80).</li>
    </ul>

    <h2>How is CGPA Calculated?</h2>
    <p>CGPA is not just a simple average of your semester GPAs. It is a <strong>credit-weighted average</strong>. This means a 4-credit core engineering subject impacts your CGPA twice as much as a 2-credit elective.</p>
    <p><em>Formula: Overall CGPA = Total Grade Points Earned / Total Credits Attempted</em></p>

    <h2>The Math Behind CGPA Recovery</h2>
    <p>To figure out what you need in the future, we use this algebraic formula:</p>
    <p><em>Required Average SGPA = [ (Target CGPA × Total Degree Credits) - (Current CGPA × Credits Completed) ] / Credits Remaining</em></p>
    <p>For example, if you have a 7.0 CGPA after 80 credits, and you want an 8.0 CGPA by the time you finish 160 credits: <br>
    Required = [(8.0 × 160) - (7.0 × 80)] / 80 = (1280 - 560) / 80 = 720 / 80 = <strong>9.0 SGPA</strong>. <br>
    You will need to maintain a brilliant 9.0 SGPA in all your remaining semesters!</p>

    <h2>Frequently Asked Questions</h2>
    <h3>Why does the calculator say my target is "Impossible"?</h3>
    <p>Because CGPA is a weighted mathematical average, it gains "momentum" over time. If you are in your final year (8th semester) and have a 6.0 CGPA, getting a 10.0 SGPA in your final semester will only pull your overall CGPA up to a 6.5. There simply aren't enough credits left to offset your past grades. In this case, you should lower your target.</p>

    <h3>Can I recover my CGPA by clearing backlogs?</h3>
    <p>Yes! Clearing a backlog replaces a 0-grade with a passing grade. This is the fastest way to artificially spike your CGPA. Check out our <a href="/tools/backlog-cgpa-calculator/">Backlog CGPA Calculator</a> to simulate this.</p>

    <h2>Related Tools</h2>
    <h3><a href="/tools/semester-gpa-required-calculator/">Semester GPA Required Calculator</a></h3>
    <p>Zoom in and figure out exactly what GPA you need for just the current semester.</p>
    <h3><a href="/tools/target-gpa-calculator/">Target GPA Calculator</a></h3>
    <p>A simpler version for calculating target GPAs based on semesters instead of credits.</p>
  </div>
""",
    "exam-passing-internal-marks-calculator": """
  <div class="rich-article-content" style="margin-top: 40px;">
    <p>University grading systems can be incredibly confusing, especially when they split your total marks into internal assessments (mid-terms, assignments, lab work) and external assessments (the final written exam).</p>
    <p>When finals approach, every student asks the exact same question: <em>"How many marks do I actually need to pass?"</em> Our <strong>Internal Marks & Final Exam Calculator</strong> removes the guesswork. It calculates the exact score you need on your final paper to pass the subject or hit a specific target grade (like an 'A' or Distinction).</p>
    
    <h2>How to Use This Tool</h2>
    <ul>
      <li><strong>Total Subject Marks:</strong> The maximum marks for the entire subject (usually 100).</li>
      <li><strong>Target %:</strong> Enter your goal. If you just want to pass, enter your university's passing criteria (e.g., 33%, 40%, or 50%). If you want a Distinction, enter 75% or 80%.</li>
      <li><strong>Your Internal Marks So Far:</strong> Sum up everything you've scored in mid-semesters, vivas, quizzes, and assignments. (Example: If you scored 18 out of 30, enter 18).</li>
      <li><strong>Final Exam Total Marks:</strong> The maximum marks of the upcoming theory paper (Example: 70).</li>
    </ul>

    <h2>Understanding the Exam Math & Split Weightage</h2>
    <p>Let's say your university uses a standard <strong>30-70 split</strong> (30 Internal, 70 External) with a 40% passing criteria out of 100 total marks. To pass the subject, you need a grand total of 40 marks.</p>
    <ul>
      <li><strong>Scenario A (Good Internals):</strong> If you scored a healthy 25/30 in your internals, you only need to score <strong>15 marks out of 70</strong> in the final exam to pass (25 + 15 = 40). This means you only need to study enough to get 21% on the final paper!</li>
      <li><strong>Scenario B (Poor Internals):</strong> If you bombed your mid-terms and only scored 5/30 in internals, you will need to score a massive <strong>35 marks out of 70</strong> in the final exam just to barely pass (5 + 35 = 40). You now have to score 50% on the final paper.</li>
    </ul>

    <h2>Frequently Asked Questions</h2>
    <h3>Can I still fail even if I reach the target marks?</h3>
    <p><strong>Warning:</strong> Always check your specific university rulebook. Many universities (especially engineering colleges under AICTE) have a <strong>"Double Passing" rule</strong>. This means you must achieve 40% overall AND a minimum of 40% strictly in the final external exam. For a 70-mark paper, this means you MUST score at least 28 marks regardless of how high your internal marks are. If you score 10/70, you will fail, even if you had 30/30 in internals.</p>

    <h3>What happens if I score a zero in internals?</h3>
    <p>If you have zero internal marks, you have to rely entirely on the final exam. If the passing mark is 40, you must score 40/70 in the final exam (which is a very difficult 57%).</p>

    <h2>Related Tools</h2>
    <h3><a href="/tools/final-grade-calculator/">Final Grade Calculator</a></h3>
    <p>If your university uses percentages and weightages instead of raw marks, use this standard US/UK calculator.</p>
    <h3><a href="/tools/college-attendance-safe-bunk-calculator/">Ultimate Attendance Calculator</a></h3>
    <p>Make sure you have enough attendance to actually sit for the final exam!</p>
  </div>
""",
    "backlog-cgpa-calculator": """
  <div class="rich-article-content" style="margin-top: 40px;">
    <p>A "backlog" (or a failed subject) is a nightmare for your academic transcript. Because you received an 'F' grade (0 grade points), but the subject credits are still counted in your total attempted credits, a backlog acts as a heavy anchor, pulling your CGPA down massively.</p>
    <p>But there is a silver lining! When you finally clear the backlog, your university generally <strong>replaces</strong> that 0 with your new passing grade. This means clearing a single high-credit backlog can skyrocket your CGPA overnight. Use our <strong>Backlog CGPA Calculator</strong> to simulate exactly how much your CGPA will jump after you pass.</p>
    
    <h2>How to Use This Calculator</h2>
    <ul>
      <li><strong>Current CGPA (with backlog):</strong> Enter the CGPA shown on your latest transcript which currently includes the F/backlog grade.</li>
      <li><strong>Total Credits Completed:</strong> The total number of credits your university has graded you on so far (make sure this includes the credits for the failed subject).</li>
      <li><strong>Credits of the Backlog Subject:</strong> Is the failed subject a minor 2-credit lab or a massive 4-credit core engineering subject? The higher the credits, the bigger the impact.</li>
      <li><strong>Expected Grade Point:</strong> What grade do you realistically think you can score when you retake the exam? (e.g., 6, 7, 8, 9).</li>
    </ul>

    <h2>Grade Replacement Policy Explained</h2>
    <p>This calculator assumes your university uses a standard <strong>Grade Replacement Policy</strong>. This is the most common system globally.</p>
    <p>Under this policy, the old "Fail" (0 points) is entirely wiped from your CGPA calculation. The denominator (Total Credits) stays exactly the same, but the numerator (Total Grade Points) increases by <code>Expected Grade × Subject Credits</code>. This is why clearing a backlog results in such a dramatic, sudden increase in CGPA.</p>
    <p><em>Note: If your university uses a Grade Averaging policy instead (where they average your F grade with your new passing grade), your CGPA increase will be exactly half of what is shown by this tool.</em></p>

    <h2>Frequently Asked Questions</h2>
    <h3>Does clearing a backlog increase CGPA more than getting an 'O' grade in a new subject?</h3>
    <p>Yes, absolutely. Clearing a backlog has a disproportionately huge impact because you are recovering lost ground. Replacing a 0 with an 8 (a +8 improvement) mathematically boosts your CGPA much faster than getting a 10 instead of an 8 in a new subject (a +2 improvement).</p>

    <h3>Will the backlog still show on my transcript?</h3>
    <p>In most universities, yes. Even after you clear it and your CGPA recovers, the transcript will usually have an asterisk (*) or a note indicating that the subject was cleared in a subsequent attempt. However, many employers only look at the final CGPA number.</p>

    <h2>Related Tools</h2>
    <h3><a href="/tools/cgpa-recovery-placement-target-calculator/">CGPA Recovery & Placement Calculator</a></h3>
    <p>Now that you've cleared your backlog, find out what you need in your remaining semesters to hit your placement target.</p>
    <h3><a href="/tools/semester-gpa-required-calculator/">Semester GPA Required Calculator</a></h3>
    <p>Calculate your target SGPA for the current ongoing semester.</p>
  </div>
""",
    "semester-gpa-required-calculator": """
  <div class="rich-article-content" style="margin-top: 40px;">
    <p>Whether you are trying to qualify for campus placements (which usually require a 7.5 or 8.0 CGPA), maintain an academic scholarship, or just stay off academic probation, knowing exactly what GPA you need in your current semester gives you a clear, actionable goal.</p>
    <p>Our <strong>Semester GPA (SGPA) Required Calculator</strong> uses a credit-weighted system to accurately tell you the exact SGPA you need to score in your current, ongoing semester to push your Cumulative GPA (CGPA) to your desired target.</p>
    
    <h2>How to Use This Tool</h2>
    <ul>
      <li><strong>Current CGPA:</strong> Your overall Cumulative Grade Point Average right now (before this semester's exams).</li>
      <li><strong>Target CGPA Goal:</strong> The overall CGPA you want to reach by the end of this semester.</li>
      <li><strong>Credits Completed So Far:</strong> Add up all the credits of the subjects you have completed in all previous semesters combined.</li>
      <li><strong>Credits in Current Semester:</strong> The total credits of the subjects you are studying right now.</li>
    </ul>

    <h2>The Math Behind Target SGPA</h2>
    <p>Because CGPA is a weighted average, we must calculate everything in terms of "Total Grade Points" to find out what you need.</p>
    <ol>
      <li><strong>Current Points:</strong> <em>Current CGPA × Credits Completed</em></li>
      <li><strong>Target Points:</strong> <em>Target CGPA × (Credits Completed + Current Semester Credits)</em></li>
      <li><strong>Points Needed:</strong> <em>Target Points - Current Points</em></li>
      <li><strong>Required SGPA:</strong> <em>Points Needed / Current Semester Credits</em></li>
    </ol>
    <p>For example, if you have a 7.0 CGPA over 40 credits, and you want a 7.5 CGPA after this 20-credit semester:<br>
    Target Points = 7.5 × 60 = 450.<br>
    Current Points = 7.0 × 40 = 280.<br>
    Points Needed = 450 - 280 = 170.<br>
    Required SGPA = 170 / 20 = <strong>8.5 SGPA</strong>.</p>

    <h2>Frequently Asked Questions</h2>
    <h3>Why is my goal "Impossible"?</h3>
    <p>Because CGPA gains "mass" or "momentum" over time. It becomes much harder to change in your later years. If you have completed 120 credits with a 6.0 CGPA, scoring a perfect 10.0 in a 20-credit semester will only pull your overall CGPA up to a 6.57. There simply aren't enough credits in the current semester to offset the massive weight of your previous 120 credits. In such cases, the calculator will inform you of the absolute mathematical maximum CGPA you can achieve.</p>

    <h3>What's the difference between SGPA and CGPA?</h3>
    <p>SGPA (Semester Grade Point Average) is your performance in one specific semester. CGPA (Cumulative Grade Point Average) is the combined average of all your SGPAs up to that point, weighted by the credits of each semester.</p>

    <h2>Related Tools</h2>
    <h3><a href="/tools/cgpa-recovery-placement-target-calculator/">CGPA Recovery & Placement Calculator</a></h3>
    <p>If your target is impossible this semester, use this tool to spread the required SGPA across ALL your remaining semesters.</p>
    <h3><a href="/tools/target-gpa-calculator/">Target GPA Calculator</a></h3>
    <p>A simpler version for calculating target GPAs based on semesters instead of credits.</p>
  </div>
"""
}

def update_html(tool_slug, new_content):
    filepath = os.path.join("tools", tool_slug, "index.html")
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the <div class="rich-article-content" ...> and replace it and everything inside it up to </article>
    # Since we know the exact structure, we can use regex
    pattern = r'<div class="rich-article-content".*?</div>\s*</article>'
    
    # We will replace it with our new_content + "\n</article>"
    replacement = new_content + "\n</article>"
    
    new_html, count = re.subn(pattern, replacement, html, flags=re.DOTALL)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated content for {tool_slug}")
    else:
        print(f"Failed to find rich-article-content in {tool_slug}")

for slug, content in tools.items():
    update_html(slug, content)
