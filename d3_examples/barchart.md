#Creating a bar chart in D3.js
The bar chart is the hello world program in d3 and it has eluded me for a long time. Looking back I think I was having a hard
time with this basic graph because I did not know the basics of  creating SVGs and the coordinate system. But I think I have it down pack now.
So lets start from the beginning.
<img src="https://smallworldbiggirl.files.wordpress.com/2012/03/sarcastic-thumbs-up.jpg" width="48">

Your data

```
var dataset =[5,10,14,25]; // the data
```

##Create the svg canvas
```
var w = 300; //width of the svg area
var h = 100; // height of the svg area
var padding =2;//
```
##Select and Append
```
var svg = d3.select("body").append("svg") // append svg element to the body
             .attr("width",w) // set the width
             .attr("height",h);// set the height
svg.selectAll("rect") // create a rectangle in the svg
```
##Data and enter
###Talk about these to methods
```
    .data(dataset) //add the data to the svg
    .enter()
    .append("rect")
```
###Setting the x coordinates for the bars
```
    .attr("x",function(d,i){//set the horizontal position of the bars
			// i = index of data set, d is the dataset
    return i *(w/dataset.length); //the index(each item in the dataset)
				//multiple that by the width of the svg/the number of elements in the dataset
				//you are spacing each of the elements equally
				// you are adjusting it dynamically
					
})

```
###setting the y coordinates for the bars
```
.attr("y",function(d){ //set the vertical positions of the bars
  return h - (d);      //remember that 0,0 is the top left of the svg canvas
		  	//adjust the bar to be on the bottom left
			//the height - the data value
})
```
h= 100 height of the entire svg
d is the elements of the dataset
so if you just return d
it would be 0,5 x,15 x,14 ... so on
but if you do h-(d) height of the viewport by the data you will get (0,95) , (x,85),(x,86)

###setting the width of the bars
```
  .attr("width",w/dataset.length-padding) //set the width of the bars
					  //the bars will have the same width
					  // add whitespace by subtracting padding
```
###setting the height of the bars
```
      .attr("height",function(d){return d}//set the height of the bars
					  // the dataset will determine the height of the bars
     )
      .attr("fill",function(d){
      return "rgb(" + (d*10)+ ",255,0)";
                 });
```





