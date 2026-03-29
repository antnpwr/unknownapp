# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
![alt text](picture/Use-case-diagram.png)

### Flowchart of the main workflow
Main Menu Flow
```mermaid
flowchart TD
    A[Start] --> B{Login Option}
    B -->|Student| C[Student Menu]
    B -->|Admin| D[Admin Menu]
    B -->|Exit| E[End]

    C -->|Logout| E
    D -->|Logout| E
```

Student Menu Flow
```mermaid
flowchart TD
    A[Student Menu] --> B{Choose Option}

    B --> C[View Course Catalog]
    B --> D[Register Course]
    B --> E[Drop Course]
    B --> F[View Schedule]
    B --> G[Billing Summary]
    B --> H[Edit Profile]
    B --> I[Logout]

    C --> A
    D --> A
    E --> A
    F --> A
    G --> A
    H --> A

    I --> End[End]
```

Admin Menu Flow
```mermaid
flowchart TD
    A[Admin Menu] --> B{Choose Option}

    B --> C[View Course Catalog]
    B --> D[View Class Roster]
    B --> E[View Students]
    B --> F[Add Student]
    B --> G[Edit Student]
    B --> H[Add Course]
    B --> I[Edit Course]
    B --> J[View Schedule]
    B --> K[Billing Summary]
    B --> L[Logout]

    C --> A
    D --> A
    E --> A
    F --> A
    G --> A
    H --> A
    I --> A
    J --> A
    K --> A
    
    L --> End[End]
```
### Prompts
```
Using the current "View all students" feature for admin, create an equivalent Python version of the program. Put the Python program in a new folder called “python.”
```