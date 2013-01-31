Photo Album Project Plan (Group 07)

Overview

The goal of the project is to develop an online version of a traditional photo album. The web application lets users
create and customize albums, share albums with friends and order for print or other related purposes. An album may
contain one or more ‘pages’, with each page containing different sizes of images and/or text.

Goals and Scope

The main objective of the project is to build a traditional album using Django. The use of javascript, Jquery, and 
Ajax will also be important to reflect the learning from the course. The project also aims to implement sharing feature
for Facebook. Flickr will be used for the image hosting. The album will have a user login through which  images can be 
added to create albums. Resizing of images will be allowed if time permits. However, image resize is not covered under
the major scope of the project.  The following will be main deliverables:
  -> a fully functional album with login and sharing option
  -> mock ups
  -> documentation
  ->source code 
  
Work practices and Tools

In the project, we will be using different tools to keep track of the project and make sure that all the requirements 
are being met at a reasonable time. All the source code will be under version control (git/github) and we aim for 
quality assurance of code coverage of about 60-80%. For time tracking and feature/task management between team members, 
we will be using a free online tool called TargetProcess. Different modes of communications will be utilized (online 
meetings, phone calls, in-person meetings) to keep the whole process going smoothly.


Project Timeline

The development of this project is going to be performed using a scrum-like process. This allows for the release of 
complete products in each release cycle, with each cycle carrying in additional features and implementation. 

Weekly Scrum
Day 1 - Planning, feature listing, prioritizing, and assigning tasks
Day 2-6- Implementation, daily checkups (online)
Day 7 - Review what’s been done and reflect on what can be done better.

We have identified three phases of development divided into five sprints:

Phase         Sprint        Duration        Release
First Phase   SPRINT 01	    28 Jan - 3 Feb	
              SPRINT 02	    4 Feb - 10 Feb	Release I
Second Phase	SPRINT 03	    11 Feb - 17 Feb	Release II
Third Phase	  SPRINT 04	    18 Feb - 24 Feb	Release III
              SPRINT 05	25 Feb - 3 Mar	Final Release

In each phase, we plan to implement the following functions and features:

              First Phase (Release I)     Second Phase (Release II)       Third Phase (Release III)
Main Task     Setup (Database, Apps)	    Page Editor	                    Advanced Image Picker (Flickr, searching, adding)
              Authentication            	Adding Images (from URL)	      Third party login - (Facebook)
              Basic album functions	      Using Layouts	                  Ordering of Albums
              Creating albums(CRUD)       Sharing Options (Social Media)	
              Creating pages (CRUD)		
              Public Album Link (unique)		

Models	      Users	                      Page_elements	                  Orders
              Albums	                    Page_layouts	                  Order_items
              Pages		

Relationship	Users have zero or          Pages have zero or many         Orders have one user
              many albums		              page_elements (images, text)
              Albums have zero or         Pages have one page_layouts     Orders have one or more order_items
              many pages	            	                                 
                                                                          Order_items have one album
                                                                          
Views	        Welcome View	              Page Editor	                    Advanced Page Editor
              Login Block	                Page Layout	                    Ordering View
              User Albums View		        Image Picker (search, adding)
              Album Editor View		
              Whole Album View		


If the project goes fluently and we had enough time, we would also like to have the fourth phase in which 
we plan to implement user defined layout for page editor (image resizing, dragging) and custom skins for albums/pages.



