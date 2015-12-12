#D3 Principles
##Selections

`d3.select("body") //selections html element`

##Append Operator
```
d3.select("body")
   .append("svg")//adds new<svg>object
    .append("rect")// adda new rectangle object in html element
  ```
##Style Operator
```
d3.select("body")
   .append("svg")//adds new<svg>object
    .append("rect")// adda new rectangle object in html element
    .attr("width",50)//set the width of our bar
    .attr("height",200)//set the height of our bar
     .style("fill","blue"); //fill the bar w/the color blue
```
