#Photo Album Project Plan (Group 07)#
================================

**Overview**

The goal of the project is to develop an online version of a traditional photo album. The web application lets users
create and customize albums, share albums with friends and order for print or other related purposes. An album may
contain one or more ‘pages’, with each page containing different sizes of images and/or text.

**Goals and Scope**

The main objective of the project is to build a traditional album using Django. The use of javascript, Jquery, and 
Ajax will also be important to reflect the learning from the course. The project also aims to implement sharing feature
for Facebook. Flickr will be used for the image hosting. The album will have a user login through which  images can be 
added to create albums. Resizing of images will be allowed if time permits. However, image resize is not covered under
the major scope of the project.  The following will be main deliverables:
  
  * a fully functional album with login and sharing option
  * mock ups
  * documentation
  * source code 
  
**Work Practices and Tools**

In the project, we will be using different tools to keep track of the project and make sure that all the requirements 
are being met at a reasonable time. All the source code will be under version control (git/github) and we aim for 
quality assurance of code coverage of about 60-80%. For time tracking and feature/task management between team members, 
we will be using a free online tool called TargetProcess. Different modes of communications will be utilized (online 
meetings, phone calls, in-person meetings) to keep the whole process going smoothly.


**Project Timeline**

The development of this project is going to be performed using a scrum-like process. This allows for the release of 
complete products in each release cycle, with each cycle carrying in additional features and implementation. 

Weekly Scrum
> - Day 1 - Planning, feature listing, prioritizing, and assigning tasks
> - Day 2-6- Implementation, daily checkups (online)
> - Day 7 - Review what’s been done and reflect on what can be done better.

We have identified three phases of development divided into five sprints:

<table>
  <tr>
    <th>Phase </th><th>Sprint</th><th>Duration</th><th>Release</th>
  </tr>
  <tr>
    <td>First Phase	</td><td> SPRINT 01 </td><td> 28 Jan - 3 Feb</td><td></td>
  </tr>
  <tr>
    <td></td><td> SPRINT 02 </td><td> 4 Feb - 10 Feb</td><td>Release I</td>
  </tr>
  <tr>
    <td>Second Phase</td><td> SPRINT 03 </td><td> 11 Feb - 17 Feb</td><td>Release II</td>
  </tr>
  <tr>
    <td>Third Phase</td><td> SPRINT 04 </td><td> 18 Feb - 24 Feb </td><td>Release III</td>
  </tr>
   <tr>
    <td></td><td> SPRINT 05 </td><td> 25 Feb - 3 Mar </td><td>Final Release</td>
  </tr>
</table>

In each phase, we plan to implement the following functions and features:

<table>
  <tr>
    <th></th><th>First Phase (Release I) </th><th>Second Phase (Release II) </th><th>Third Phase (Release IIII) </th>
  </tr>

   <tr>
    <td>Main Task </td>
    <td> 
     Setup (Database, Apps)<br /> Authentication <br /> Basic album functions <br /> 
     Creating albums / viewing / editing / deleting (CRUD) <br /> Creating pages (CRUD) <br /> Public Link (unique)
    </td>
    <td> 
     Page Editor <br />  Adding Images (from URL) <br />  Using Layouts <br />  Sharing Options (Social Media)
     </td>
     <td>
     Advanced Image Picker (Flickr, searching, adding) <br />  Third party login - (Facebook) <br /> Ordering of Albums
    </td>
  </tr>
  <tr>
    <td>Models</td>  
    <td> Users <br /> Albums<br /> Pages </td>
    <td> Page_elements <br />Page_layouts </td>
    <td>Orders <br />Order_items </td>
  </tr>
   <tr>
    <td>Relationship</td>  
    <td> 
    Users have zero or many albums<br />
    Albums have zero or many pages 
    </td>
    <td> 
    Pages have zero or many page_elements (images, text) <br />
    Pages have one page_layouts 
    </td>
    <td>
    Orders have one user <br />
    Orders have one or more order_items <br />
    Order_items have one album
    </td>
  </tr>
   <tr>
    <td>Views  </td>  
    <td>         
    Welcome View <br />
    Login Block <br />
    User Albums View <br />
    Album Editor View <br />
    Whole Album View 
    </td>
    <td> 
    Page Editor <br />
    Page Layout 

    </td>
    <td>
    Advanced Page Editor <br />
    Ordering View <br />
    Image Picker (search, adding)

    </td>
  </tr>
</table>
		
If the project goes fluently and we had enough time, we would also like to have the fourth phase in which 
we plan to implement user defined layout for page editor (image resizing, dragging) and custom skins for albums/pages.


#Albumr Final Report(Group 07)#
================================

**Group Members**

- Lulit Gebremichael (336127)
- Xinjie Duan (205944)

**Responsibilities**

Xinjie
> - Design user interface
> - Write templates, related CSS and some Javascript;
> - Implement "Third Party Login" function
> - Implement "Share public links in social media" function;
> - Check the validation of HTML and CSS
> - Manual test

Lulit
> - UI Implementation and Design
> - Implement All Album Functionalities (Albumr App)
> - Write unit tests

**User Guidelines**

----------

    	Public Link:  http://boiling-mountain-8053.herokuapp.com/

-------



-  Regiter and login to the site by signing up or using a third-party login
   After successful login, you will be redirected to home view.
-  Press the 'create new album' button to create a new album
-  Fill out Album essentials and press submit. You will be directed to the home view. 
-  From the list of your own albums, choose the album you want to edit and press edit. You will be redirected to the album
   editor view
   In the album editor view:
   - Press '+' sign to add pages to your album
   - You can edit page related information from the right side bar
   - Change the caption of the page as necessary
   - Choose from different layout templates (currently 3) to design  your page
   - To add/change images, click on the area of the page in the editor you want to change the image of.
      You will notice that the selected area's background has changed (darkened)
      Go to the right side bar, and copy/paste the desired image url in the image url field
      You will see that the image has been added to your page
   - Remember to press save to save all your changes
   - You can browse between pages by selecting the box that contains the page number (1, 2, 3..)
   - You can delete a page by pressing 'x' found in the upper right corner of each page
- You can share albums by clicking the 'share' link for the desired album. You will be redirected to the public view of
   the album. In there, you can use social share buttons or copy the link url to share the album between friends
- You can delete albums by clicking the 'delete' link for the desired album.
   

**Final Remarks**

Even though we hadn't managed to use our time properly, we had managed to develop a working MVP that we believe should satify 
the requirements of this work. We had implemented all the basic features, and other external features such as third party login,
sharing in social networks, ajax. Furthermore, we have used Knockoutjs, a MVVM based JS framework which helped to structure our 
client-side code greatly and also increase the usability of the site.

Looking back, organizing our work in TDD mode might have helped us to write tests more and not to reverse-engineer test cases.
Currently, our code coverage lies around 30%, which is less than ideal.

One of the problems we have also encountered was at the final deployment stage. We were not able to properly serve static files 
in Heroku enviornment. Thus, we have opted to deploy the application in debug mode, which is less than ideal. We will 
try to figure out the problem and submit the corrections before demo day.







