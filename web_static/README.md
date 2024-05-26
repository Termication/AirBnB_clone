# Introduction

This directoru provides a comprehensive guide on HTML and CSS, covering essential concepts and practical examples. Whether you're a beginner or looking to refresh your knowledge, this guide will help you understand the basics of web development.
## Table of Contents

    What is HTML
    How to Create an HTML Page
    What is a Markup Language
    What is the DOM
    What is an Element/Tag
    What is an Attribute
    How Does the Browser Load a Webpage
    What is CSS
    How to Add Style to an Element
    What is a Class
    What is a Selector
    How to Compute CSS Specificity Value
    What are Box Properties in CSS

## What is HTML

HTML (HyperText Markup Language) is the standard language for creating web pages. It describes the structure of a webpage using a series of elements (or tags).
How to Create an HTML Page

To create an HTML page, you need to write HTML code and save it with a .html extension. Here’s a simple example:

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first HTML page.</p>
</body>
</html>
```

## What is a Markup Language

A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. HTML is a type of markup language used to structure content on the web.
What is the DOM

The DOM (Document Object Model) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM is a representation of the document as a tree of objects.
What is an Element/Tag

An HTML element is defined by a start tag, some content, and an end tag. For example, <p>This is a paragraph.</p> is a paragraph element. Tags are the HTML keywords (surrounded by angle brackets) used to create elements.
What is an Attribute

Attributes provide additional information about HTML elements. They are always included in the opening tag and usually come in name/value pairs like name="value". For example, <a href="https://www.example.com">Visit Example</a> uses the href attribute.
How Does the Browser Load a Webpage

### When you load a webpage, the browser performs the following steps:

    The browser sends a request to the server for the webpage.
    The server sends back the HTML file.
    The browser parses the HTML, creating the DOM.
    The browser sends requests for additional resources (CSS, JavaScript, images).
    The browser parses CSS and applies styles.
    The browser executes JavaScript.
    The browser renders the page to the user.

## What is CSS

CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML. CSS controls the layout of multiple web pages all at once.
How to Add Style to an Element

You can add styles to an HTML element using CSS in three ways:

    Inline CSS: Adding styles directly in the HTML element.

    html

<p style="color: red;">This is a red paragraph.</p>

Internal CSS: Adding styles within a <style> tag in the HTML document's <head>.

```html

<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
```

External CSS: Linking an external CSS file.

```html

    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
```
## What is a Class

A class is an attribute used in HTML and CSS to define a group of elements that share the same style. Classes are defined using the class attribute in HTML and are prefixed with a dot (.) in CSS.

Example:

```html

<p class="intro">This is an introductory paragraph.</p>
```
```css

.intro {
    font-size: 20px;
    color: green;
}
```

## What is a Selector

A CSS selector is a pattern used to select the elements you want to style. Common types of selectors include:

    Element Selector: Selects all elements of a given type.

```css

p {
    color: blue;
}
```

### Class Selector: Selects all elements with a specific class.

```css

.intro {
    font-size: 20px;
}
```

### ID Selector: Selects an element with a specific ID.

```css

    #header {
        background-color: yellow;
    }
```

### How to Compute CSS Specificity Value

CSS specificity determines which styles are applied to an element when multiple rules match. Specificity is calculated based on the types of selectors used:

    Inline styles have the highest specificity (e.g., style="...").
    IDs have higher specificity than classes.
    Classes have higher specificity than elements.

### Example specificity calculation:

    #header (ID) has a specificity of 100.
    .intro (class) has a specificity of 10.
    p (element) has a specificity of 1.

## What are Box Properties in CSS

The CSS box model describes the rectangular boxes generated for elements in the document tree and is composed of:

    Content: The actual content of the box, where text and images appear.
    Padding: Clears an area around the content. The padding is transparent.
    Border: A border that goes around the padding and content.
    Margin: Clears an area outside the border. The margin is transparent.

### Example:

```css

div {
    width: 100px;
    padding: 10px;
    border: 5px solid black;
    margin: 20px;
}
```

This guide covers fundamental concepts of HTML and CSS to help you get started with web development. For more detailed information, refer to the official HTML and CSS documentation.
