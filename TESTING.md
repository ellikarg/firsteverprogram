# Alessio Mida -  Testing

[Back to README](README.md)


![finished_site](https://github.com/ellikarg/firsteverproject/assets/132999023/ff1544d5-2710-4520-89ff-560afb546bc7)

Visit the deployed site: https://ellikarg.github.io/firsteverproject/index.html

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

### Python Testing

### PEP8 Testing

- - -

## MANUAL TESTING

### Manual Python Testing


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
