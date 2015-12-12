#SVG Objects
SVG standards for scalar vector graphics
SVG is rendered with the browser and the html of the page
Doesn't get distored like raster images

SVG are three different things
* Shapes-polygon
* Filters-blur/ drop shadow
* Gradients-linear or radial gradients another way of painting

SVG

##HTML
```
<svg>
	<rect width="50" height="200" style="fill:blue;"/>

</svg>

```

##D3.js
```
d3.select("body")
   .append("svg")//adds new<svg>object
    .append("rect")// adda new rectangle object in html element
    .attr("width",50)//set the width of our bar
    .attr("height",200)//set the height of our bar
     .style("fill","blue"); //fill the bar w/the color blue
```

It looks nicer in html :)

SVG coordinate system
same as every computer graphics coordinate system
* 0,0 is on the top left corner.
* 1,0 is on the top right corner
* 0,1 is the bottom left corner
* 1,1 is on the bottom right corner

