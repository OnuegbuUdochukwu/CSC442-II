**FACULTY OF PHYSICAL SCIENCES**

**DEPARTMENT OF COMPUTER SCIENCE**

CSC 442 --- Computational Biology & Interdisciplinary Studies

**PROGRAMMING ASSIGNMENT**

**PROJECT 1**

**Microscope Specimen Size Calculator**

|                      |                              |
|----------------------|------------------------------|
| **Academic Session** | 2024/2025                    |
| **Semester**         | Second Semester              |
| **Level**            | 400 Level                    |
| **Submission**       | As directed by your lecturer |

*This is an individual assignment. All work must be your own.*

**Assignment Overview**

In microscopy, the image you observe through a microscope lens is a magnified version of the real specimen. Your task is to build a software application that takes the measured size of a specimen as seen through a microscope and calculates its true real-world size. You will develop this application progressively across five phases, each building on the last, beginning from a simple command-line program and ending with a live, hosted web application.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Core Scientific Formula</strong></p>
<p>Real Size = Measured Size (mm) ÷ Magnification Factor</p>
<p>The magnification factor depends on the type of microscope used. Different microscopes</p>
<p>provide different levels of magnification, and your application must account for this.</p></td>
</tr>
</tbody>
</table>

**The Task**

You are required to build this application in five phases as described below. You must complete all five phases. Each phase must be fully working before you move on to the next.

**(a) Core Calculation Program**

Write a Python program that:

- Accepts the size of a specimen as measured from a microscope image.

- Accepts the type of microscope being used --- this must be a selection from a predefined list (not a free-text entry), because different microscopes have different magnification factors, and your program must determine the correct magnification factor automatically based on the type selected.

- Calculates the real-life size of the specimen.

- Allows the user to choose the unit in which the result is displayed (for example: nm, µm, mm, cm, m).

- Displays the result along with a clear breakdown showing how the answer was calculated.

**(b) Database Integration**

Extend your program from (a) to include a database that records each calculation performed. The database must store the following for every calculation:

- The username of the person who performed the calculation

- The specimen size that was entered (the microscope image size)

- The actual real-life size that was calculated

**Note:** Users must input their username before performing any calculation. The program must also provide a way to view and manage the saved records.

**(c) Python-Based GUI**

Extend your program from (b) to include a graphical user interface (GUI) built using Python. The GUI must replace the command-line interaction entirely. All functionality from phases (a) and (b) must be accessible through the GUI. The following are required as part of the interface:

- A field for the user to enter their username.

- The ability to upload an image of the specimen (the user browses and selects an image file from their computer).

- A dropdown list for selecting the microscope type.

- A dropdown list for selecting the output unit.

- A display area for the calculated result.

- Access to the saved records database (view history and manage entries).

**(d) Web-Based GUI**

Change your program to use a web-based GUI instead of the Python-based GUI from phase (c). The web application must provide all the same functionality as your Python GUI.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Important Note from Lecturer</strong></p>
<p>The files used for implementing the Python-based GUI from phase (c) must still be present</p>
<p>in your project folder even though they are no longer involved in running the application.</p>
<p>These files will be inspected during marking.</p></td>
</tr>
</tbody>
</table>

**(e) Free Hosting**

Host your web application on the internet using a free hosting platform so that it is publicly accessible via a URL. Your hosted application must be fully functional --- all features, including image upload and the database, must work correctly after deployment.

**Additional Requirements**

The following requirements apply across all phases of the project and must be incorporated into your design:

- The user must upload the specimen image and input the measured microscope size as part of the calculation process.

- The microscope type must always be selected from a dropdown list --- never typed manually. Different microscopes have different magnification factors, and your application must determine and apply the correct factor automatically based on the selection.

- Users must input their username whenever they perform a calculation.

- The user must be able to select the unit of the output from a dropdown list (e.g., nm, µm, mm, cm, m).

**Marking Scheme**

| **Component**            | **What is assessed**                                                                                                                             | **Marks** |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **(a) Core Calculation** | Correct formula, microscope type dropdown with magnification mapping, unit selection and conversion, formula breakdown display, input validation | **20**    |
| **(b) Database**         | Stores username, specimen size and actual size per calculation; records retrievable and manageable                                               | **15**    |
| **(c) Python GUI**       | All required interface elements present; image upload with preview; dropdowns for type and unit; result display; database history view           | **20**    |
| **(d) Web GUI**          | Full web interface replicating Python GUI functionality; Python GUI files retained in project folder                                             | **25**    |
| **(e) Hosting**          | Application publicly accessible via URL; all features functional after deployment                                                                | **15**    |
| **Code Quality**         | Readable code, logical structure, appropriate comments, clean user experience                                                                    | **5**     |
| **TOTAL**                |                                                                                                                                                  | **100**   |

*End of Assignment*
