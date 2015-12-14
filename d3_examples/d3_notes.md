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

##Select vs SelectAll
http://bost.ocks.org/mike/nest/
There is an important difference between select and selectAll: select preserves the existing grouping, whereas selectAll creates a new grouping. Calling select thus preserves the data, index and even the parent node of the original selection!

###What is grouping?
If any body is familar with adobe photoshop or illustrator it is similar to that.
The SVG <g> element is used to group SVG shapes together. Once grouped you can transform the whole group of shapes as if it was a single shape. This is an advantage compared to a nested <svg> element which cannot be the target of transformation by itself.

https://www.dashingd3js.com/svg-group-element-and-d3js
