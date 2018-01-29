---
Title: ASNA Visual RPG for the Web
Published: 2016-06-02
Tags: introduction
Category: AVR
Order: 10000
---


# ASNA Visual RPG for the Web



### Welcome!  

ASNA Visual RPG (AVR) is the only RPG compiler available for .NET. It snaps into Visual Studio (VS 2015 or VS2017) and with it you can create Web services, Windows Forms apps, and ASP.NET Web Forms apps. AVR uses ASNA DataGate to connect to either the IBM i or MS SQL Server to provide real-time, read/write database access. AVR can also make program calls (with Call/Parm) to the IBM i program objects (these calls occur with subsecond response times and are a great way to integrate existing logic and DB access with AVR) and stored procedures that return scalar values.  

This site provides guidance and technical explanations on how to use ASNA Visual RPG to create ASP.NET Web sites.  

### Introduction to Web applications

These materials don't assume much Web developer experience. If you're experienced with Web development, but not AVR, you can skim through them pretty quickly. If you're new to Web development, you're in for a fun ride! Build Web apps isn't just good for business, it's tons of fun. Note that these documents don't provide all that you'll need to know about Web development; these docs are mostly AVR-specific and there is lots more you'll need to learn--especially with respect to JavaScript, HTML, and CSS. Those skills are platform agnostic--and are covered well in many third-party books and videos.  

Web applications are distinct from fat Windows clients and green-screen in many ways. Here are a few considerations:

* **Web apps are inherently stateless**. To master ASP.NET you need to clearly understand the constraints and issues statelessness imposes on application design. Each Web page is essential its own little activation group with its own lifecycle. For any one page, a DB connection is established, files are opened and possibly written to, the files are closed, and the DB connection is disconnected. Any data on one page must be explicitly made available to other pages--the default behavior is that data from any one page (except that data explicitly persisted to disk) is "released" when the next page is requested. 

* **Web apps work across HTTP**. This is generally transparent to the AVR programmer, but it's important to remember that a Web app is more sensitive to network traffic and slow networks than other application types. For example, in the old green-screen days, it was possible (both physically and practically) to hundreds or even thousands of rows in a subfile. For Web work, and especially mobile Web work, that isn't practical--it would most likely impede performance to the point of major user frustration. Testing for performance is a critical aspect of Web applications. 

* **Web apps require close attention to security**. Web applications are published to the Internet (as opposed to your own private intranet) and therefore naturally have a exposure to every script kiddie, hacker, and malcontent that lurks. Some security concerns are addressed within the application itself (with user authentication and authhorization) and some are external to the application (such as using HTTPS and firewalls). 

* **A Web application's user interface comprises three pillars**. A modern Web page isn't simply HTML, it's also CSS and, in virtually every case, JavaScript.   

	* [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) defines the structure and content of a page. Generally you'll be using HTML in your AVR Web apps. 
	* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) defines the design and display of the page. We recommend the popular CSS framework Bootstrap but you can opt to write your own or use any of the other popular CSS open-source libraries. 
	* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS) defines the behavior of the page.   
    
* **Target multiple clients**. A Windows fat client or a green-screen RPG program both target very specific devices. A Web app targets a more general-purpose device: the Web browser. Therefore, you may build AVR Web apps that run on desktops, phones, and/or tablets. Web apps that are expected to work across different devices need to be responsive(https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode). 
