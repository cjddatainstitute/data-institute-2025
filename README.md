# Data Institute 2025
For students of [The Data Institute](https://cjddatainstitute.org/), a collaboration between the Center for Journalism & Democracy and the Ida B. Wells Society for Investigative Reporting.

We'll use this page to add all the materials used to teach the [2025 Data Institute](https://cjddatainstitute.org/2025/): slides, exercises, links, and homework. This is not an online course and won't have all the context or instruction to be a standalone class.

Want to use our slides? Our teaching materials fall under the [Creative Commons license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/).

# Curriculum

## Table of Contents
- [Install Party](#welcome-reception--install-party)

Week 1:
- [Day 1: Intro to Data Journalism, Spreadsheets, Best Practices](#day-1)
- [Day 2: Evaluating Data, Open Refine, Analyzing One Variable](#day-2)
- [Day 3: Tabula, AI, and Putting It All Together](#day-3)
- [Day 4: Visualizing Data, Charts and Maps](#day-4)
- [Day 5: Intro to Code, How Websites Work, HTML, CSS](#day-5)


Week 2:
- [Day 6: Intro to Design, Make Your Own Website](#day-6)
- [Day 7: Web Scraping, Fundamentals of Programming](#day-7)
- [Day 8: Even More Web Scraping](#day-8)
- [Day 9: Continuing Learning / Field Trip](#day-9)
- [Day 10: Celebration: Final Show & Tell](#day-10)

## Welcome Reception & Install Party

**ACCOUNTS**
<ul>
  <li><a href="https://github.com/join?source=header-home">Github.com</a><br>(Make sure to confirm your e-mail address)</li>
  <li><a href="https://accounts.google.com/SignUp?service=wise&amp;continue=https%3A%2F%2Fdrive.google.com%2F%23&amp;ltmpl=drive">Google.com</a></li>
  <li><a href="https://app.datawrapper.de/signin">Datawrapper</a></li>
</ul>

**SOFTWARE**
- <a href="https://www.google.com/chrome/browser/desktop/">Google Chrome</a> - Everything we'll be teaching you about previewing and testing code will work in other browsers like Firefox, Safari, and Internet Explorer, but each browser can work a little differently. Since we'll be demoing everything in Chrome, it'll make it easier to follow along if you have it installed.
- Slack (<a href="https://itunes.apple.com/app/slack/id803453959?ls=1&amp;mt=12">Mac</a>, <a href="https://slack.com/ssb/download-win">Windows</a>) - All of you should have received an invite to join the Data Institute Slack. If you've never used Slack before, it's basically a place where you can message with a group of people. You need both an account (which you should be able to set up based on your email invitation) and we want you to download the desktop app (which you can do by clicking on the Mac or Windows link above).
- Sublime Text (<a href="https://www.sublimetext.com/download_thanks?target=mac">Mac</a>, <a href="https://www.sublimetext.com/download_thanks?target=win-x64">Windows</a>) - This app is where we're going to be writing all our code. It's completely free, and will occassionally ask you if you'd like to pay, but payment is not required. For both beginners and experts, Sublime is one of the best apps for coding.
- <a href="https://desktop.github.com/">Github Desktop App</a> - an app to simplify your Github experience.
- Tabula (<a href="https://github.com/tabulapdf/tabula/releases/download/v1.2.1/tabula-mac-1.2.1.zip">Mac</a>, <a href="https://github.com/tabulapdf/tabula/releases/download/v1.2.1/tabula-win-1.2.1.zip">Windows</a>) - Your best friend for when you have a huge stack of data tables in PDF format and need to turn it into actual data you can use.
- Open Refine (<a href="https://openrefine.org/post_download?version=3.8.1&platform=mac">Mac</a>, <a href="https://openrefine.org/post_download?version=3.8.1&platform=win-with-java">Windows</a>) - A great tool to help you clean data (ex: it can recognize that "Saint Paul" and "St. Paul" maybe refer to the same city in Minnesota)
	- If you're on a Mac, and you get the error that Google/Open Refine is damaged, [follow these instructions](open-refine-troubleshooting.md).

<hr/>

## Day 1
Monday, July 7

### Intro to Data Journalism
<a href="https://propublica.s3.amazonaws.com/data-institute/intro-to-data-2025.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/intro-to-data.jpg"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/Intro-to-spreadsheets-2025.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/intro-to-spreadsheets.jpg"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/finding-data-2023.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/finding-data.jpg"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/loading-data%202023.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/loading-data.jpg"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/best-practices-2025.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/best-practices.jpg"></a>
<a href="https://projects.propublica.org/graphics/images/data-institute/presentations/2019/string-functions.pdf"><img width="300" src="https://projects.propublica.org/graphics/images/data-institute/presentations/2019/string-functions.jpg"></a>

[More about data diaries](https://cronkitedata.github.io/cronkite-docs/general/04-data-diary.html).

## Day 2
Tuesday, July 8

<a href="https://propublica.s3.amazonaws.com/data-institute/evaluating-data-2025.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/evaluating-data.jpg"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/data-integrity-2025.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/data-integrity.png"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/open-refine-2025.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/open-refine.jpg"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/analysis-one-var-25.pdf"><img width="300" src="https://projects.propublica.org/graphics/images/data-institute/presentations/2019/one-var.jpg"></a>

<a href="https://github.com/cjddatainstitute/data-institute-2025/blob/ca8d9ff6d3941f20b15b375370d47e228d09997f/assets/Georgia_spending_OpenRefine.csv">Georgia Spending csv for OpenRefine exercise</a>

## Day 3
Wednesday, July 9

<a href="https://propublica.s3.amazonaws.com/data-institute/Data%20Institute%20Tabula.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/data-institute-tabula.png"></a>
<a href="https://docs.google.com/presentation/d/1k_Mui_M5SeDKGyhbAdFw-awfDHHYoOoRHiLrv_FGtRg/edit"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/extractive_ai.png"></a>
<a href="https://propublica.s3.amazonaws.com/data-institute/2024%20Analysis-grab-bag.pdf"><img width="300" src="https://propublica.s3.amazonaws.com/data-institute/data-analysis-grab-bag.png"></a>

<a href="https://wmata.com/about/transit-police/upload/Blotter-June-17-2024.pdf">Initial Tabula exercise: Police blotter</a>

<a href="https://github.com/cjddatainstitute/data-institute-2025/blob/main/assets/hinesville-ga-fire-hydrant-list-12-19-2023.pdf">Extra Tabula exercise: Extract fire hydrant locations</a>

## Day 4
Thursday, July 10

### Visualizing Data, Charts and Maps
Morning session

Discussion: <a href="https://github.com/cjddatainstitute/data-institute-2025/blob/7f4bc7364fb660f83c3b7f7e4b776d77cb3a9e78/assets/why_to_visualize_data.pdf">Why to visualize data</a>

<a href="https://docs.google.com/presentation/d/17euyzEe1WQMfu061vZhZg-OopQG0pdB2WgQAhry1v9Y/edit"><img width="500" src="https://github.com/cjddatainstitute/data-institute-2024/blob/main/assets/day-4-thumbnail.png"></a>

Afternoon session

Intro to visualizing data
- [Creating your first chart](https://academy.datawrapper.de/article/245-how-to-create-your-first-datawrapper-chart)
	- [Download aquifer use data for creating your first chart](https://github.com/cjddatainstitute/data-institute-2025/blob/1b7e96c5b035687dc2c0c6308a597e075e6e5854/assets/Georgia%20aquifer%20withdrawals.xlsx)

[Create a map in Tableau!](https://public.tableau.com/app/discover) 
- [Files for creating your first map with Tableau](https://github.com/brionesb1116/tableau-workshop)

## Day 5
Friday, July 11

### Intro to Code
<a href="https://projects.propublica.org/graphics/images/data-institute/presentations/2017/intro-to-code.pdf"><img width="500" src="https://projects.propublica.org/graphics/images/data-institute/presentations/intro-to-code.jpg"></a>

**In-Class Demos**
- What coding languages have you heard of?
- Using the web inspector

### How Websites Work
<a href="https://projects.propublica.org/graphics/images/data-institute/presentations/2017/how-websites-work.pdf"><img width="500" src="https://projects.propublica.org/graphics/images/data-institute/presentations/2017/how-websites-work.jpg"></a>

### HTML
<a href="https://projects.propublica.org/graphics/images/data-institute/presentations/2017/html.pdf"><img width="500" src="https://projects.propublica.org/graphics/images/data-institute/presentations/html.jpg"></a>

**In-Class Demos**
- How to create your first HTML file
- Shortcut to the basic HTML template
- How to use:
  - `<h1>`
  - `<h2>`
  - `<h3>`
  - `<p>`
- Let's look up together:
  - `<img>`
  - `<a>`
- Can you figure out:
  - How do you make a bulleted list?

**Exercises**
<ul>
  <li>Can you fix this <a href="https://codepen.io/sisiwei/pen/PNvaeB?editors=1000">broken code</a>? </li>
</ul>

### Basic CSS
<a href="https://projects.propublica.org/graphics/images/data-institute/presentations/2017/css.pdf"><img width="500" src="https://projects.propublica.org/graphics/images/data-institute/presentations/2017/css.jpg"></a>

**In-Class Demos**

- How to create your first CSS file
- Shortcut to linking to your CSS file
- How CSS styles work

### Optional Homework
Copy and paste <a href="https://codepen.io/sisiwei/pen/KzLezJ?editors=1000">this code</a> and follow the instructions inside to format the page.

## Day 6
Monday, July 14

### Intro to Design

Follow Michael's slides here:

<a href="https://docs.google.com/presentation/d/13tTHJbmM2fg03qqMKX9vIg1evrBX_B9ZqMV3ms9dr9U/edit?slide=id.g357ba6e2f8e_1_35#slide=id.g357ba6e2f8e_1_35"><img width="504" alt="Michael_Grant_Intro_Design_DI25" src="https://github.com/user-attachments/assets/30dae103-fc78-4bd8-b61c-0f73a5058322" /></a>

Check out Lena's resources here:

<a href="https://lenagroeger.com/design_workshop/data-institute-2024#/"><img width="500" src="https://static.propublica.org/projects/datainstitute/intro-to-design.png"></a>



### Make Your Own Website
<a href="https://pages.github.com/"><img width="500" src="https://static.propublica.org/projects/datainstitute/github-pages.jpg"></a>



<!-- <a href="https://docs.google.com/presentation/d/1TsY4Jqd9mO_kahmkXvHKbMu4B8e1xctb9Mz6LXjMbtY/edit?pli=1#slide=id.g1d0b3f77a7_0_0"><img width="500" src="https://static.propublica.org/projects/datainstitute/design_concepts_lecture.png"></a>

<a href="https://docs.google.com/presentation/d/1-5mC4tJUvLRRRvlsmZe9Eng_Pjd91w05e9RcHSH5Tjo/edit#slide=id.g1d0b3f77a7_0_0"><img width="500" src="https://static.propublica.org/projects/datainstitute/design_concepts_exercise.png"></a>

<a href="https://docs.google.com/presentation/d/1jgz0mG72wxiEtLJzhbiTLuocIPZF8jSYtIvWfDTE2e4/edit#slide=id.g1d0b3f77a7_0_0"><img width="500" src="https://static.propublica.org/projects/datainstitute/design_concepts_your_turn.png"></a>
 -->


## Day 7
Tuesday, July 15

### Web Scraping + Fundamentals of Programming
**In-Class Demos**
<ul>
  <li>Rich's slides on <a href="https://drive.google.com/file/d/1jT0BgpGqNszvyx4CNFefZYaixvs1Jidl/view?usp=sharing">Introduction to Web Scraping</a></li>

<a href="https://drive.google.com/file/d/1jT0BgpGqNszvyx4CNFefZYaixvs1Jidl/view?usp=sharing">
<img width="500" alt="Rich_Fundamentals_WebScraping_DI25" src="https://github.com/user-attachments/assets/31f82b8e-3c8c-446a-bddb-b791a2cda109" /></a>
<li>Chrome plugin: <a href="https://instant-data-scraper.en.softonic.com/chrome/extension">Instant Data Scraper</li>
<li><a href="https://www.parsehub.com/">Parsehub</a></li>
</ul>



## Day 8
Wednesday, July 16

### Web Scraping with Python

**Morning session**
<ul>
  <li>Discussion: How and why do reporters and news outlets use programming? Why not use no-coding tools?</li>
  <li><a href="https://github.com/cjddatainstitute/data-institute-2025/blob/a4069941701151ec0dc3a446411ffac2b2661c7a/python_files/goals_and_jargon.md">Goals for the day and intro to jargon</a></li>
  <li>Editing and running Beyoncé-related code in <a href="https://github.com/features/codespaces">Github Code Spaces</a></li>
</ul>

<ul>
  <li>Scrape a website and <a href="https://github.com/cjddatainstitute/data-institute-2025/tree/main/python_files">save the data to a .csv</a>
  
</ul>

***Bonus / on your own / discusssion***
<ul>
	<li>Set up and run Palewire's <a href="https://palewi.re/docs/first-web-scraper/">First Web Scraper</a>. You can set this up on your own computer instead of in the cloud.</li>
	<li>Some agencies <i>want</i> to share data with you. Look up how to access an API with Python and grab <a href="https://enfo.gaepd.org/api-docs/index.html">Georgia EPD Enforcement Orders</a></li>
</ul>

**Afternoon session**

<a href="https://github.com/cjddatainstitute/data-institute-2025/tree/main/real-estate-gentrification-analysis-main">Data analysis with Python notebooks</a>

***Bonus / on your own***
<a href="https://palewi.re/docs/first-python-notebook/index.html">First Python Notebook</a>

## Day 9
Thursday, July 17

### Field trip day!

On Thursday, July 17, we'll meet in our usual workspace at 9:30 a.m. for some open work time and discussion. Around 12:30 p.m., we'll break for lunch, before everyone explores Atlanta. 

Shameless plug: [The High Museum’s Dataverse exhibit](https://high.org/exhibition/ryoji-ikeda/) is currently underway!
Admission is free on the [second Sunday](https://high.org/event-category/for-families-and-kids/ups-second-sundays/) and [third Wednesday](https://high.org/event-category/free-admission/#:~:text=Free%20Admission%20Events,UPS%20Second%20Sunday) of the month.

## Day 10
Friday, July 18

### Celebration and final show & tell

We'd love to hear a highlight of something you've learned from the Data Institute. Each person will have about 5 minutes to jump to the front of the room, plug in your laptop if youd like to, and share something you're excited about.

This is super laid back and celebratory! You could talk about anything:

* a project you've been working on for a while, and now you have new ideas to try
* a project you've been wanting to work on but felt stuck, and now you've figured out the right next step
* a class you've been teaching that you're ready to bring these concepts into
* something you learned at the institute that you really loved and keep thinking about

Again, this is *very* informal. A moment to celebrate what we learned, and share some of your own work with the rest of the cohort. We can chat more about this throughout the institute. Feel free to reach out with any questions any time!
