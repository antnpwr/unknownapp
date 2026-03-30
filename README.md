# unknownapp
This is an unknown application written in Java

### Use Case Diagram
![alt text](picture/Use-case-diagram.png)

### Flowchart of the main workflow
```mermaid
flowchart TD
    A[Start] --> L{Login?}
    L -->|1| U[Student Login]
    L -->|2| C1[Admin Login]
    L -->|3| X[Exit]
    X --> END[End]

    U --> U1[Enter ID or 'new']
    U1 --> U2{Is 'new'?}
    U2 -->|Yes| U3[Create Profile]
    U2 -->|No| U4{Student exists?}
    U4 -->|No| L
    U4 -->|Yes| SM[Student Menu]

    U3 --> U31{Valid Input?}
    U31 -->|No| L
    U31 -->|Yes| SM

    SM --> SChoice{Select Option}

    SChoice -->|1| S1[View Course Catalog]
    S1 --> SM

    SChoice -->|2| S2[Register Course]
    S2 --> S21[Enter Code]
    S21 --> S22{Empty?}
    S22 -->|Yes| SM
    S22 -->|No| S23[Process Registration]
    S23 --> S24{Success?}
    S24 -->|Yes| SM
    S24 -->|No| SM

    SChoice -->|3| S3[Drop Course]
    S3 --> S31{Has courses?}
    S31 -->|No| SM
    S31 -->|Yes| S32[Enter Code]
    S32 --> S33{Empty?}
    S33 -->|Yes| SM
    S33 -->|No| S34[Process Drop]
    S34 --> SM

    SChoice -->|4| S4[View Schedule]
    S4 --> SM

    SChoice -->|5| S5[Billing Summary]
    S5 --> SM

    SChoice -->|6| S6[Edit Profile]
    S6 --> S61[Enter New Data]
    S61 --> SM

    SChoice -->|7| S7[Save Data]
    S7 --> L

    C1 --> A1[Enter Password]
    A1 --> A2{Correct?}
    A2 -->|No| L
    A2 -->|Yes| AM[Admin Menu]

    AM --> AChoice{Select Option}

    AChoice -->|1| A11[View Course Catalog]
    A11 --> AM

    AChoice -->|2| A21[Enter Course Code]
    A21 --> A22{Course exists?}
    A22 -->|No| AM
    A22 -->|Yes| A23[Display Roster]
    A23 --> AM

    AChoice -->|3| A31[View All Students]
    A31 --> AM

    AChoice -->|4| A41[Enter Student Data]
    A41 --> A42{Valid?}
    A42 -->|No| AM
    A42 -->|Yes| AM

    AChoice -->|5| A51[Enter Student ID]
    A51 --> A52{Exists?}
    A52 -->|No| AM
    A52 -->|Yes| A53[Edit Info]
    A53 --> AM

    AChoice -->|6| A61[Enter Course Data]
    A61 --> A62{Valid?}
    A62 -->|No| AM
    A62 -->|Yes| AM

    AChoice -->|7| A71[Enter Course Code]
    A71 --> A72{Exists?}
    A72 -->|No| AM
    A72 -->|Yes| A73[Edit Course]
    A73 --> AM

    AChoice -->|8| A81[Enter Student ID]
    A81 --> A82{Exists?}
    A82 -->|No| AM
    A82 -->|Yes| A83[Show Schedule]
    A83 --> AM

    AChoice -->|9| A91[Enter Student ID]
    A91 --> A92{Exists?}
    A92 -->|No| AM
    A92 -->|Yes| A93[Show Billing]
    A93 --> AM

    AChoice -->|10| A10[Save Data]
    A10 --> L
```
### Prompts
Using the current "View all students" feature for admin, create an equivalent Python version of the program. Put the Python program in a new folder called “python.”
