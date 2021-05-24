Live Link - [https://d-and-d-pocket-book.herokuapp.com/](https://d-and-d-pocket-book.herokuapp.com/)

---

## **Table of Contents**

---

- [Overview](#overview)
- [UX](#ux)
  - [Stories](#stories)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Wireframes](#wireframes)
- [Features](#features)
- [Testing](#testing)
  - [Bugs](#bugs)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Project barriers and the solutions](#project-barriers-and-the-solutions)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Support](#support)

---

## **Overview**

---

The Dungeons and Dragons Pocket book is an application designed for note taking in a more streamlined, structured user firendly way.

The UX is focused on being able to create and edit a list of characters and games and storing detailed notations.

---

## **UX**

---

### **Stories**

#### **User Stories**

"So much happened during our last session I couldnt write it all down quickly enough”

“My notes have no sense of order or logic to them, I need a better system”

“I cant remember where we met that character in the story, or what he/she said”

#### **Developer Stories**

"I learned to play D&D recently so learning coding at the same time has intwined them both in my current learning. 
I felt it appropriate to combine these two passions into one project"

"D&D is very complex, as is coding. This being my first project working with databases, I felt that using the game 
as a basis for building my project would be both challenging and engaging."

"Whilst playing the game I often hear my fellow players struggling to remember things and also sifting through
through their notes looking for something specific. I feel this app fill a real need for D&D enthusiasts"

### **Strategy**

#### **Project Goals:**

I believe this project fits a real need in the tabletop community and has potential to expand its functionality and scope.
My main focus of this project is to achieve proof of concept and see how the project performs among my peers.

- The application to be responsive on all devices to wether the user is playing in person or online they will have easy access
- Ther user to be able to create a list of all their games and characters, and input data to be easily recalled when needed.
- 
- Create a database that will allow unique users to control and manipulate as they see fit

#### **User Goals:**

- C
- C
- C
- Create an enjoyable, interactive and responsive experience
- Provide a template to progress through the riddle
- Expand their thought processes through the required logical elimination required for completion

---

[Return to Table of Contents](#table-of-contents)

---

### **Scope**

#### **Planned Functionality:**

Login-Register Page:

- 
- 
- 
-  

Profile Page:

- 
- 
- 
- 

Game Page:

- 
- 
- 
- 

Character Page:

- 
- 
- 
- 

Galaxy Page:

- Paragraph emerges from the galaxy centre with an introduction to the riddle
- Header with the riddle title drops down onto the screen from above
- Footer with contact and social links rises from below
- Social links that will open a new tab to the relevant page
- When the "Good Luck!" button is pressed, the header and footer return off-screen and the introduction paragraph returns to the centre of the galaxy. The background zooms in to create the illusion of the user being sucked to the centre along with the paragraph.

Riddle Page:

- Explanation box that details the riddle as well as user instructions
- Start button that removes the explanation box and begins the timer
- Back button returns the user to the galaxy page
- Riddle expands out from the centre of the screen
- Table of input elements for answers
- Information section with interactive multiple panel viewing
- Clues list are bullet-pointed and cross out when the corresponding answers are entered
- Hint section for the user if they are struggling
  - Text changes depending on how far along the user is in the riddle
- Before a user can view the hint there is a box to attempt to convince the user to try a bit harder before asking for a clue
- Notepad panel so the user can type any notations they feel necessary for progression
- Timer to record how long completion takes
- When the user enters an answer, the information section automatically switches to the clues section
- Picture of Einstein that rotates between several images
- The picture changes in reaction to a users action
- Winks when a correct answer is entered
- Angry face when an incorrect answer is entered
- Demonised face when the user attempts to break the game
- When a user completes the riddle, the Einstein clapping gif replaces the Einstein picture
- If a user attempts the same answer multiple times, inputs are disabled, Einstein image changes to a demonised caricature, a reset button emerges and a warning message appears scolding the user
- On completion of the riddle the clue-controls panel is replaced but the congratulations panel, which consists of "Welcome to the 2%" spinning text, social links, background image of a confetti gif and three buttons
  - Reset - Reloads the page
  - Back to Galaxy - Returns the user to the galaxy page
  - Feed the Cat - Which removes the fish gif and plays the cat audio for comic effect 

---

[Return to Table of Contents](#table-of-contents)

---

### **Structure**

#### **Interaction Design:**

Login-Register Page:

- 
- 
- 
-  

Profile Page:

- 
- 
- 
- 

Game Page:

- 
- 
- 
- 

Character Page:

- 
- 
- 
- 

Galaxy Page:

- When the user presses the "Good Luck!" button, the header and footer return off the screen and as we see the introduction panel return into the galaxy, the background image increases in size creating the illusion that the user is also entering the centre of the galaxy. After the animation finishes the user is forwarded to the riddle page.
- The email address in an anchor with mailto tags for users default mail application to create a blank email directly
- The social link icons are anchors to my personal profiles page on the respective outlets

Riddle Page:

- The explanation panel has two buttons. Start - Back
  - Start - Removes the box and the user may begin the riddle
  - Back - Returns the user to the galaxy page
- There are twenty-five input elements for answering the riddle, all of which cause the page to respond depending on the input.
- There are three buttons in the controls section. Hint - Clues - Notepad
- Hint - the hint checker box obscures the hint and double checks the user does indeed need a hint.
  - Yes, I am hopelessly lost - reveals the hint based on the user's current answers
  - No, I will try harder - changes the panel to no-hint which displays "Excellent choice, I am so proud."
- Clues - Shows a list of the 15 clues and the question of the riddle "Who owns the fish?"
- Notepad - A textarea box appears that the user can type notes into if needed
- If the user enters the same answer 3 times a reset button appears where the clues-controls div is located, where that the user can press to reload the page
- When the user completes the riddle the clues-control div is replaced by the congratulations panel which has three buttons. Reset - Back to Galaxy - Feed the Cat
  - Reset - reloads the page
  - Back to Galaxy - returns the user to the galaxy page
  - Feed the Cat - Removes the fish gif and plays the cat audio, purely for satire purposes

#### **Information Design:**

Login-Register Page:

- 
- 
- 
-  

Profile Page:

- 
- 
- 
- 

Game Page:

- 
- 
- 
- 

Character Page:

- 
- 
- 
- 

Galaxy Page:

- The header states the title of the web application - The Einstein Riddle
- The introduction paragraph states the purpose of and the theorized success rate of the riddle.
- The footer contains the creator's contact information and anchors to their corresponding profiles to the relevant icon

Riddle Page:

- Explanation panel emerges from the centre of the screen to explain the riddle and give some friendly advice to the user
- The Einstien pictures serve as a prompt to the user depending on what actions they take
  - Wink - the user has entered a correct answer
  - Angry face - the user has entered an incorrect answer
  - Einstein clapping gif - the user has completed the riddle
  - Cheat pic - A demonised version of the caricature when the user attempts to break the ha,e
- Clues panel bullet points the 15 clues and highlights the riddles question.
- Hints checker offers the user to either confirm they want a clue or opt-out
  - Yes, I am hopelessly lost - reveals the hint based on the user's current answers
  - No, I will try harder - changes the hint text to " Excellent choice, I am so proud."
- Hint panel shows the user a clue that is relevant depending on the current level of progression

---

[Return to Table of Contents](#table-of-contents)

---

### **Skeleton**

- [Wireframes](#wireframes)
- Introduction page with simple header and footer with social links
- Riddle page with 3 sections
- Responsive Einstein Image that reacts to users interactions
- Interactive panel that switches depending on users actions and buttons pressed
- Riddle answer table, 5 rows, 6 columns, 5 row titles, 25 inputs

[Return to Table of Contents](#table-of-contents)

---

### **Surface**

#### **Images**

Galaxy: The initial page (index.html) begins with a spiral galaxy, and the introduction emerging from its centre.

Einstein: The caricature rotates between different versions of the same image as the user progresses through the riddle. The picture responds when there is a correct or incorrect input entered and if the user attempts to keep inputting answers sequentially.

#### **Colours**

The galaxy page uses the colour scheme of the gif itself to compliment each other

The Einstein page is kept a simple yellow to try and focus the users' attention on the pictures and animations of the pictures and input elements

#### **Typography**

- "Titillium" font (san serif as backup) for index.html.
- "cursive" font (san serif as backup) for riddle.html.

---

[Return to Table of Contents](#table-of-contents)

---

## **Wireframes**

---

![alt_text](assets/images/wireframes/wireframe-1.png "image_tooltip")

![alt_text](assets/images/wireframes/wireframe-2.png "image_tooltip")

![alt_text](assets/images/wireframes/wireframe-3.png "image_tooltip")

---

[Return to Table of Contents](#table-of-contents)

---

## **Features**

---

### **Existing Features**

- Designed with HTML5, CSS3 and JavaScript.
- 2 separate HTML pages.
- Timer
- Table of input elements

### **Features Left to Implement when skills develop**

- This web application is only responsive on desktop and mid-size device screens. Since I have not used a frontend framework for this project making it responsive was a challenging but an enlightening experience. At a later date when my css skills have progressed further, I will return and make the application responsive on all devices.
- Currently, the game has its flaws the users can take advantage of, the user can just enter every possible answer into a single input until they discover the correct one. Due to time constraints and limited knowledge, I have struggled to come up with a solution that does not involve being overly harsh on the user.
- At a later date I wish to implement different versions of this riddle, for example, a Lord of the Rings themed version where it is Gandalf instead of Einstein and the error tone would be replaced by a line from the film "Fool of a Took!"
- Varying degrees of difficulty
  - Hard mode would not give the user any confirmation of a right or wrong answer until the end
  - Easy mode would give the user prompts and more obvious clues.

---

[Return to Table of Contents](#table-of-contents)

---

## **Testing**

---

### **Screen Testing**

Checked compatibility in Safari, Chrome, Firefox

#### Google Chrome Developer Tools - Device frames tests

- iPad
- iPad Pro

#### [Media Genisis Responsiveness Checker](https://responsivedesignchecker.com/)

#### Desktop Screen Sizes

- 24" - 1920x1200
- 23" - 1920x1080
- 22" - 1680x1050
- 20" - 1600x900

#### Notebook Sizes

- 15" - 1366x768
- 13" - 1024x800
- 10" - 1024x600

#### Tablet Screen Sizes

- iPad Mini - 768x1024
- iPad Retina - 768x1024
- iPad Pro - 1366x1024
- Kindle Fire - 768x1024
- Kindle Fire HD - 768x1024
- Asus Eee - 768x1024
- Nexus 7 - 600x960
- Nexus 9 - 1024x768
- Galaxy Tab 10 - 800x1280

I have tested the website on various physical devices (iPad, iPad Air, Macbook Pro)

### **Validator**

HTML - [W3C](https://validator.w3.org/) - Markup Validation

CSS - [W3C](https://jigsaw.w3.org/css-validator/) - CSS Validation

JS - [JSHint](https://jshint.com/) - JS Validator

### **Defensive Design**

- If a user attempts to enter the same answer in multiple boxes, the entire riddle will be disabled and an onscreen message with a giant reset button will show on the screen.
- Ensuring all target="\_blank" links are accompanied by rel="noreferrer".
- Designing the site to be comfortably navigated without having to use the back button in the browser interface.

---
### Manual Testing 
---

#### **Galaxy**

- "Good Luck!" button initiates the animation and correctly opens up riddle.html after the designated time delay has passed.
- All social links open a new tab to my profile on the designated media site

#### **Riddle**

- Start button removes the explanation panel and begins the timer
- Back button initiates the animation and returns the user to the galaxy page
- Each input element responds as expected when the correct answer is entered
  - Nationality changes to the corresponding flag
  - Input element background, border and text colour change to highlight the corresponding colour
    - House icons also change to the corresponding colour and initiates animation
  - Pet sounds of the corresponding animal sound on input
  - Smoking gif displays in the background
  - Specific beverage image replaces the input
- Einstein image winks when a correct answer is entered
- When the user enters an incorrect...
  - The error tone plays
  - The input element clears
  - The angry face image is injected into the Einstein picture rotation
- When all correct answers are entered...
  - The Einstein image is replaced by a clapping gif
  - Celebration by Kool and the Gang plays
  - Celebration panel is displayed
  - Background image for each panel is changed to confetti gif
- When the hint button is pressed...
  - All other potential panels are removed
  - Displays the hint panel
  - Displays the hint checker
    - Hint checker buttons...
      - Yes, I am hopelessly lost - reveals the hint based on the user's current answers
      - No, I will try harder - changes panel to "no-hint"
  - Hint button is disabled
- When the clues button is pressed...
  - All other potential panels are removed
  - Displays the hint panel
  - Clues button is disabled
- When the notepad button is pressed...
  - All other potential panels are removed
  - Displays the textarea
  - Notepad button is disabled
- When the user enters an answer...
  - the information section automatically switches to the clues section
    - When the user is on notepad it switches back to clues
    - When the user is on hints, hint checker or no hint it switches back to clues
- When a user enters the same answer 3 times...
  - All input elements are disabled
  - The breaking-game-warning appears with its animation
  - The clues-control panel is removed and replaced with the reset button image
    - Pressing the reset button picture reloads the page
  - The Einstein picture is replaced by the cheat pic

---

### **Bugs**

---

#### **Found**

1. Timer buttons would stop working if the play button was pressed twice
2. The audio files would not play, and console test eg(console.log(cats.duration)) were returning NaN
3. The hint checker "No, I will try harder" changes the text of the hint to "Excellent choice, I am so proud" but doesn't if the user does decide to opt for the hint later it does switch back to the original hint.
4. window.location objects work within GitPod but when pushed to GitHub the live site threw back a 404 error
5. When being viewed on an iPad, the url and tab bar were preventing the user from being able to access the bottom input elements without the keyboard being on the screen.

#### **Resolution**

1. This was caused as the code snippet created a new instance every time the play button was pressed, so 2 or more presses on the play button caused the pause and reset button to affect the subsequent instances rather than the first
2. It just turned out the file path was incorrect, the code was correct otherwise
3. Created another div ("no-hint") that displays instead of the hint div
4. Swapping the objects for document.location.href and location.reload() resolved the issue
5. I commented out the overflow:hidden in both css files to allow the user to scroll if needed.

#### **Unresolved**

- The site is not as responsive as I would like, medium-size device screens in portrait are not ideal, but due to time constraints and my skill limitations, I was unable to make it fully responsive.
- While testing the device on my iPad, I realised my css was being overwritten. When input was disabled due to a correct answer, the element appearing to be slightly transparent. Due to time constraints, I could not resolve this issue.

[Return to Table of Contents](#table-of-contents)

---

## **Technologies Used**

---

### **1. Languages**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### **2. Integrations**

- [jQuery](https://jquery.com) by linking via jQueryCDN to HTML Doc.
- [FontAwesome](https://fontawesome.com/) Icons for links in Footer.
- [Google Fonts](https://fonts.google.com/) - Overall Typography import.

### **3. Workspace, version control and Repository storage**

- [GitPod](https://github.com/mkuti/corklagos-venture/blob/master/gitpod.io) - Main workspace IDE(Integrated Development Environment)
- [Git](https://git-scm.com/) - Distributed Version Control tool to store versions of files and track changes.
- [GitHub](https://github.com/) - A cloud-based hosting service to manage my **Git** repositories.

---

[Return to Table of Contents](#table-of-contents)

---

## **Resources**

---

- [Code Institute Course Content](https://courses.codeinstitute.net/)
- Code Institute **SLACK Community**
- [Stack Overflow](https://stackoverflow.com/) - General resource.
- [Youtube](https://www.youtube.com/) - General resource.
- [CSS-Tricks](https://css-tricks.com/) - General resource.
- [W3.CSS](https://www.w3schools.com/w3css/4/w3.css) - General resource.
- [Balsamiq](https://balsamiq.com/wireframes/) - Wire-framing design tool.
- Unicorn Revealer - Chrome Extension
- ColorZilla - Chrome Extension

---

[Return to Table of Contents](#table-of-contents)

---

## **Project barriers**

---

- JavaScript has been a challenging language to learn, there are so many different approaches that will lead you to the same result. (eg. initially, I was writing out long functions with multiple if statements, but as time went on I started learning how to refactor my code into a loop) The biggest lesson I have learned is to always try to achieve the result in as few lines as possible.
- I decided to build the project without Bootstrap to test my css skills, although I have learned a lot from this route, I will be using a framework going forward to cover the heavy lifting.
- Responsiveness was always going to be a challenge from the nature of what I wanted to achieve, especially without a frontend framework, it slowed down my progress but did allow me to increase my knowledge and gain a greater appreciation for frameworks.
- I used someone else's code for the timer (timer.js) and taking that and using it to suit my purposes was challenging. The original author's code has specific HTML requirements which caused issues when trying to adapt to my own.
- The hintSwitcher function was tricky, as there are multiple routes to get to the final answer. Designing a function to cover all these routes was a challenge.

---

[Return to Table of Contents](#table-of-contents)

---

## **Deployment**

---

GitPod was used to write all code in this repository and pushed via Git to GitHub.

### **GitHub**

- When viewable HTML files have been pushed to GitHub, select 'Settings' the last item in the repository navbar.
- Under 'Github Pages' and 'Source' there should be a drop-down menu with 'None' selected by default.
- After you press the drop-down menu and select 'master', then press save.
- Once saved, this will shortly publish the project to GitHub Pages and the site URL will be available in the 'GitHub Pages' in 'Settings'.

### **Local Download/Clone**

- You can do this by opening the repository, clicking on the 'Code' button with the download icon and selecting either 'clone or download'.
- The Clone option provides a URL, which you can use on your desktop IDE.
- The Download ZIP option provides a link to download a ZIP file that can be unzipped on your local machine.
- User needs to open the unzipped folder and open index.html for the homepage to populate.

---

[Return to Table of Contents](#table-of-contents)

---

## **Credits**

---

### **Media**

Pictures

- Site background image from [giphy](https://giphy.com/gifs/universe-spiral-galaxy-star-cluster-vortex-konczakowski-3og0IFrHkIglEOg8Ba)
- Einstein Images
  - [Main drawing](https://in.pinterest.com/pin/253257179017742853/) <br>
    (All variations of this image were edited privately)
  - [Clapping GIF](https://wifflegif.com/gifs/662977-albert-einstein-insanity-gif)
- [Confetti gif](https://gifer.com/en/6k2)
- [Wrong Answer picture](https://lipmag.com/wp-content/uploads/2016/05/A_frightened_and_an_angry_face_left_and_right_respectively._Wellcome_V0009326.jpg)
- [Reset Button](https://i.pinimg.com/originals/40/94/fc/4094fc29f32df934851e7aad83b33a81.jpg)

Sound Files

- [Animal Sounds](https://www.freesoundeffects.com/free-sounds/animals-10013/)
- [Celebration - Kool & The Gang](https://vimeo.com/335541134)
- [Wrong Answer Audio](https://www.youtube.com/watch?v=36_bISAhExo)

### **Code Snippets**

The timer function (timer.js) was taken from... <br>
https://tinloof.com/blog/how-to-build-a-stopwatch-with-html-css-js-react-part-2/

---

[Return to Table of Contents](#table-of-contents)

---

## **Acknowledgements**

---

### I would like to thank

- **Guido Cecilio** - My mentor, for his time and guidance.
- **Sean Murphy** - For his knowledge and reliable feedback.
- **Anthony O’Brien** - For his expertise in the industry.
- **CI staff** and **Slack Community** for round the clock reliability and helpfulness.

---

## **Support**

---

If you require any help or assistance you may contact me on

john.doyle.mail@icloud.com

---