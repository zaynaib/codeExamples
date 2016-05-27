<!--- Please insert your code here --->

<!DOCTYPE html>
<html lang = "en">
	<cfinclude template="header.cfm" >
   
   <body id = "home" data-spy ="scroll" data-target=".navbar" data-offset="200">
   	<!-- nav bar -->
<nav class="navbar navbar-dark bg-primary navbar-fixed-top">
	<button class="navbar-toggler hidden-sm-up" type="button" data-toggle="collapse" data-target="#collapsingNav">
    &#9776;
  </button>
	 
	<div class="container collapse navbar-toggleable-xs" id="collapsingNav">
		
  <ul class="nav navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#home">Home <span class="sr-only">(current)</span></a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#about">About</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#speakers">Speakers</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#schedule">Schedule</a>
    </li>
  </ul>
  <a class="navbar-brand pull-sm-right m-r-0 hidden-xs-down" href="http://www.teamtreehouse.com">Presented by Treehouse</a>
</div>
</nav><!-- end of nav bar -->

<!-- jumbotron -->
<div class="jumbotron jumbotron-fluid bg-info">
	<div class="container text-sm-center p-t-3">
		<h1 class="display-2">Full Stack Conf</h1>
		<p class="lead">A One-day Conference About all Things JavaScript!.</p>
		
		<div class="btn-group m-t-2" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#register">Register Now</button>
  <a class="btn btn-secondary btn-lg" href="#speakers">See Speakers</a>
</div>
	</div>
	
</div><!-- /jumbotron -->



   	<div class="container p-t-2">
   		<!---about--->
   		<div id="about"class="row">
   			<div class="col-lg-4 ">
   				<h3 class="m-b-2">About Full Stack Conf</h3>
   				<img class="m-b-1 img-fluid img-rounded" src="img/pdx.jpg" alt="Portland">
<p>The beautiful city of Portland, Oregon will be the host city for Full Stack Conf!</p>
<p>Explore the future of JavaScript with a lineup of industry professionals. Discover new techniques to advance your career as a web developer.</p>
   			</div>
   			<div class="col-lg-4 ">
   				<h3 class="m-b-2">Expert Speakers</h3>
<p>Our expert speaker lineup was just announced, so don't wait too long before grabbing your tickets!</p>
<p>Want to meet the international JavaScript community and share skills with some of the world's top experts, hackers, and makers? Be the first to know what to expect for the future of JavaScript.</p>
<p>Full Stack Conf is committed to being inclusive and welcoming for everyone. We look forward to another intensive day of learning and sharing.</p>
   			</div>
   			<div class="col-lg-4 ">
   				<h3 class="m-b-2">What You'll Learn</h3>
<div class="list-group">
  <a href="#" class="list-group-item"><strong>MongoDB</strong>: NoSQL database</a>
  <a href="#" class="list-group-item"><strong>Angular</strong>: JavaScript framework </a>
  <a href="#" class="list-group-item"><strong>Express</strong>: Framework for Node</a>
  <a href="#" class="list-group-item"><strong>Node.js</strong>: JavaScript environment</a>
  <a href="#" class="list-group-item"><strong>ES2015</strong>: Latest version of JavaScript</a>
  <a href="#" class="list-group-item"><strong>Babel</strong>: JavaScript compiler</a>
</div>
   			</div>
   		</div><!---about--->
   		
   		<!---speakers--->
   		<h1 id="speakers" class="display-4 text-xs-center m-y-3 text-muted">Speakers</h1>
   		<div class="row">
   			
  <div class="col-md-6 col-lg-4 clearfix">
  	<div class="card">
  <img class="card-img-top img-fluid" src="img/angie.png" alt="Card image cap">
  <div class="card-block">
    <h4 class="card-title">Angie McAngular</h4>
    <p class="card-text">Angie is a web developer and teacher who is passionate about building scalable,data driven web apps, especially ones that address old problems with new tech!</p>

  </div>
</div>
  </div> <!-- end of div -->


  <div class="col-md-6 col-lg-4 clearfix ">
  			<div class="card">
  <img class="card-img-top img-fluid" src="img/nodestradamus.png" alt="Card image cap">
  <div class="card-block">
    <h4 class="card-title">NodeStradamus</h4>
    <p class="card-text">NodeStra is a software engineer and philosopher trying to leave the world better than he found it. He codes for non-profits, eCommerce, and large-scale web apps.</p>

  </div>
  	
  </div>
  </div>

  <div class="col-md-6 col-lg-4 clearfix ">
  			<div class="card">
  <img class="card-img-top img-fluid" src="img/geo.png" alt="Card image cap">
  <div class="card-block">
    <h4 class="card-title">Geo "Lo" Cation</h4>
    <p class="card-text">Geo is a JavaScript developer working on large-scale applications. He's also a teacher who strives to support students in removing all barriers to learning code.</p>

  </div>
  </div>
</div>

  <div class="col-md-6 col-lg-4 clearfix ">
  			<div class="card">
  <img class="card-img-top img-fluid" src="img/ecma.png" alt="Card image cap">
  <div class="card-block">
    <h4 class="card-title">Ecma Scriptnstuff</h4>
    <p class="card-text">Jay is a developer, author of CSS: The Missing Manual, JavaScript &amp; jQuery: The Missing Manual, and web development teacher.</p>

  </div>
  </div>
</div>

  <div class="col-md-6 col-lg-4 clearfix ">
  			<div class="card">
  <img class="card-img-top img-fluid" src="img/jay.png" alt="Card image cap">
  <div class="card-block">
    <h4 class="card-title">Jay Query</h4>
    <p class="card-text">Jay is a developer, author of CSS: The Missing Manual, JavaScript &amp; jQuery: The Missing Manual, and web development teacher.</p>

  </div>
  </div>
</div>

 <div class="col-md-6 col-lg-4 clearfix ">
  			<div class="card">
  <img class="card-img-top img-fluid" src="img/json.png" alt="Card image cap">
  <div class="card-block">
    <h4 class="card-title">Json Babel</h4>
    <p class="card-text">All of his professional life, Json has worked with computers online; he is a polyglot programmer and likes using the right tools for the job.</p>

  </div>
  </div>
</div>


<!-- /speakers -->
   		
   		<!--- callout button--->
   		<button type="button" class="btn btn-info-outline btn-lg center-block m-y-3"> Don't Miss Out Register Now</button>
   		
   		<!---schedule--->
   		<h1 id="schedule" class="display-4 text-xs-center m-y-3 text-muted">Schedule</h1>
   		
   		
   		<ul class="list-group ">
   			
   		
   			
   			
   			
   			
   			
<li class="list-group-item ">
   			 <div class="media">
  <a class="media-left" href="#">
    <img class="media-object" src="img/nodestradamus.png" alt="Generic placeholder image" height="64" width="64">
  </a>
  <div class="media-body">
    <h4 class="media-heading">Keynote: Internet of Things  <span class="label label-info label-pill pull-xs-right">9:00am</span></h4>
<p>Nodestradums</p>
  </div>
</div>
   			
   		</li>
   		
   		<li class="list-group-item">
   				 <div class="media">
  <a class="media-left" href="#">
    <img class="media-object" src="img/angie.png" alt="Generic placeholder image" height="64" width="64">
  </a>
  <div class="media-body">
    <h4 class="media-heading">Angular Basics <span class="label label-info label-pill pull-xs-right">10:00am</span></h4>
<p>Angie McAnuglar</p>
  </div>
</div>
   			
   		
		</li>
		
		<li class="list-group-item">
			
					 <div class="media">
  <a class="media-left" href="#">
    <img class="media-object" src="img/jay.png" alt="Generic placeholder image" height="64" width="64">
  </a>
  <div class="media-body">
    <h4 class="media-heading">Hey, Mongo! <span class="label label-info label-pill pull-xs-right">11:00am</span></h4>
<p>Jay Query</p>
  </div>
</div>
			
			
			
			
			
		
		</li>
		<li class="list-group-item list-group-item-success">
   		 <h4 class="list-group-item-heading">Lunch Break! <span class="label label-info label-pill pull-xs-right">12:00pm</span></h4>
 			 Free Pizza for Everyone!
		</li>
   		
   		
 	<li class="list-group-item">  		
 		
 				 <div class="media">
  <a class="media-left" href="#">
    <img class="media-object" src="img/ecma.png" alt="Generic placeholder image" height="64" width="64">
  </a>
  <div class="media-body">
    <h4 class="media-heading">Introducing ES2015 <span class="label label-info label-pill pull-xs-right">10:00am</span></h4>
<p>Ecma Scriptnstuff</p>
  </div>
</div>
 		
 		
 		
 		
 		
 
	</li>
	<li class="list-group-item">
		
				 <div class="media">
  <a class="media-left" href="#">
    <img class="media-object" src="img/geo.png" alt="Generic placeholder image" height="64" width="64">
  </a>
  <div class="media-body">
    <h4 class="media-heading">Gettin' MEAN <span class="label label-info label-pill pull-xs-right">10:00am</span></h4>
<p>Geo "Lo" Cation</p>
  </div>
</div>
		
		
		
		
		
		
  		
	</li>
	<li class="list-group-item">
		
				 <div class="media">
  <a class="media-left" href="#">
    <img class="media-object" src="img/json.png" alt="Generic placeholder image" height="64" width="64">
  </a>
  <div class="media-body">
    <h4 class="media-heading">What's Babel? <span class="label label-info label-pill pull-xs-right">10:00am</span></h4>
<p>Json Babelr</p>
  </div>
</div>
		
		
	</li> 
	</ul><!--/schedule -->

<!-- callout button -->

<button type="button" class="btn btn-info-outline btn-lg center-block m-y-3" data-toggle="modal" data-target="#register"> Don't Miss Out, Register Now </button>

   		
   		<!-- signup form -->
<hr>
<div class="row p-y-2 text-muted">
  <div class="col-md-6 col-xl-5">
    <p><strong>About Treehouse</strong></p>
    <p>Treehouse brings affordable technology education to people everywhere to help them achieve their dreams and change the world.</p>
  </div>
  <div class="col-md-6 col-xl-5 col-xl-offset-2">
    <p><strong>Stay up-to-date on Full Stack Conf</strong></p>
    <div class="input-group">
      <input type="text" class="form-control" placeholder="Email">
      <span class="input-group-btn">
        <button class="btn btn-primary" type="button">Sign up</button>
      </span>
    </div>
  </div>
</div>
<hr><!-- /signup form -->
   	
   	
   	<!-- footer-->
   	<div class="row p-y-1">
  <div class="col-md-7">
  	<ul class="nav nav-inline">
  <li class="nav-item">
    <a class="nav-link" href="#">Community</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Tracks</a>
  </li>
  <li class="nav-item">
    <!-- Split button -->
<div class="btn-group dropup" role="group" aria-label="other conferences">
  <button type="button" class="btn btn-secondary">Other Confs</button>
  <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">CSS Conf</a>
    <a class="dropdown-item" href="#">Python Conf</a>
    <a class="dropdown-item" href="#">Java Conf</a>
   
    <a class="dropdown-item" href="#">Swift Conf</a>
 
</div>
</div>
  </li>
  
</ul>

  </div>
  
  <div class="col-md-5 text-md-right">
    <small>&copy; 2016 Full Stack Conf &amp; Treehouse</small>
  </div>
</div>
   	<!-- /footer -->
   	
   	</div> <!---.container--->
   	<!--
   	
   	  FORM MODAL
   	-->
   	
   	<div id="register" class="modal fade">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header bg-info">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
        <h4 class="modal-title">Register for Full Stack Conf</h4>
      </div>
      <div class="modal-body">
        <!--- registration form --->
        <form>
        	<div class="alert alert-warning alert-dismissible fade in" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
  <strong>Hurry! </strong> Early Bird Registration ends in 2 days.
</div>
        	<h5 class="m-b-2">Basic Info</h5>
  <fieldset class="form-group">
    <label for="name">Name</label>
     <input type="text" class="form-control" id="name" >
  </fieldset>
  <fieldset class="mail has-danger">
    <label for="mail">Email:</label>
    <input type="email" class="form-control form-control-label corm-control-danger" id="mail" >
  </fieldset>
  
  <fieldset class="form-group">
  	<label for="role"> Job Role:</label>
  	<select class="form-control c-select" id="role" name="user_role">
  		<option value="full stack js developer">Full Stack JavaScript Developer</option>
		<option value="front end developer">Front End Developer</option>
		<option value="back end developer">Back End Developer</option>
		<option value="designer">Designer</option>          
		<option value="student">Student</option> 
  		
  	</select>
  	</fieldset>
  	<hr class="m-y-2">
  		<h5 class="m-b-2">Which Topics Interest You Most?</h5>
  		<div class="form-group c-inputs-stacked">
  			<label class="c-input c-checkbox">
  				<input type="checkbox">
  					<span class="c-indicator"></span>
  					JavaScript Frameworks
  			</label>
  			
  			<label class="c-input c-checkbox">
  				<input type="checkbox">
  					<span class="c-indicator"></span>
  					JavaScript Libraries
  			</label>
  			
  			<label class="c-input c-checkbox">
  				<input type="checkbox">
  					<span class="c-indicator"></span>
  					Node.js
  			</label>
  			
  			<label class="c-input c-checkbox">
  				<input type="checkbox">
  					<span class="c-indicator"></span>
  					Build Tools
  			</label>
  			
  			<label class="c-input c-checkbox">
  				<input type="checkbox">
  					<span class="c-indicator"></span>
  					ES2015
  			</label>
  		</div>
  		
  		<hr class="m-b-2">
  			<h5 class="m-b-2"> Payment Info</h5>
  			<div class="row">
  <div class="col-lg-6 form-group">
    <label for="cc-num">Card Number:</label>
    <input class="form-control" id="cc-num" type="text">
  </div>

  <div class="col-lg-3 form-group">
    <label for="zip">Zip Code:</label>
    <input class="form-control" id="zip" type="text">
  </div>

  <div class="col-lg-3 form-group">
    <label for="cvv">CVV:</label>
    <input class="form-control" id="cvv" type="text">
  </div>
</div>


<div class="row">
	<label class="col-lg-12"> Expiration Date:</label>
	<div class="form-group col-lg-8">
		<select class="c-select form-control" id="exp-month">
  <option value="1">1 - January</option>
  <option value="2">2 - February</option>
  <option value="3">3 - March</option>
  <option value="4">4 - April</option>
  <option value="5">5 - May</option>
  <option value="6">6 - June</option>
  <option value="7">7 - July</option>
  <option value="8">8 - August</option>
  <option value="9">9 - September</option>
  <option value="10">10 - October</option>
  <option value="11">11 - November</option> 
  <option value="12">12 - December</option>                           
</select> 
	</div>
	<div class="form-group col-lg-4">
		<select class="c-select form-control" id="exp-year">
  <option value="2016">2016</option>
  <option value="2017">2017</option>
  <option value="2018">2018</option>
  <option value="2019">2019</option>
  <option value="2020">2020</option>                          
</select>  
	</div>
	
</div>

<hr class="m-b-2">
	<button type="submit" class="btn btn-primary btn-lg">Register </button>
</form>
        
        
         <!--- /registration form --->
        
        
        
        
        
      </div>
      
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
   	
   		 <!---jQuery for bootstrap--->
   		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
   </body>
</html>