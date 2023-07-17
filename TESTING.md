# Travel Cost Calculator -  Testing

[Back to README](README.md)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Lighthouse](#lighthouse)
  * [WAVE Testing](#wave-testing)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

During development I made use of Google Chrome Developer Tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected. The automated and manual testing was unfortunately only done at the end.

I have gone through each page using Google Chrome Developer Tools to ensure that each page is responsive on a variety of different screen sizes and devices.


- - -

## AUTOMATED TESTING

### PEP8 Testing

The code was passed through the [PEP8 linter](https://pep8ci.herokuapp.com/) and there are no problems
<details><summary>Testing Result</summary>
<img src = "docs/pep8_testing"></details>

- - -

## MANUAL TESTING

### Manual Python Testing

I have manually tested this project by doing the following:
- given invalid inputs: when the user inputs invalid data she/he is notified and asked to try again
- tested in my loval terminal and the Code Institute Heroku terminal

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | One bug that I spent a lot of time fixing on was that the gallery pictures would overlap the h3-headings when displayed in the grid with only one column (for small screens) | In the end I managed to fix it with a really good hint from my mentor: using the dev tools to make a border around each div-container of the grid-structure and then consequently checking all margin- and padding- and gap-values for the different screen sizes and how they behave when changed from one to another. |
| 2 | Another bug that took me a bit to solve was the round image-container on the index page, because it would always loose its shape when viewed on different screen sizes although I had given it a fixed size | In the end I watched many flex-box tutorials and when my mentor showed me the help with the borders around the flexbox-items, I understood that I have to use another div-element as flex-element in order for the round image-container not to be responsive, but the div around it. |


- - -

### Known Bugs

| No | Bug | |
| :--- | :--- | :--- |
| 1 | Two of the gallery images were oversized on the iPhone 8 in the safari browser | Strangely, on an iPhone SE (also in the safari browser), this was not a problem at all. |
