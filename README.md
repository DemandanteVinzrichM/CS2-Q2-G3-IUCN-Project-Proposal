# 📌 Computer Science 2 - Drafted Project Proposal

## 📝 Project Title
Philippine Biodiversity Taxonomic Finder (with IUCN Conservation Status Integration)

## 📃 Project Description
The Philippine Biodiversity Taxonomic Finder is an interactive Python 3 console application designed to help students, researchers, and nature enthusiasts explore endemic Philippine wildlife. The program allows users to select an animal from an organized menu, view its complete scientific classification (taxonomy), and check its official International Union for Conservation of Nature (IUCN) conservation status.

## 🔍 Problem Statement
Many students and wildlife advocates lack a centralized, quick-access digital tool to look up structured scientific information—such as hierarchical taxonomy and extinction risk—specifically tailored to endemic Philippine biodiversity. Scattered data sources make learning about local endangered species inefficient. This program addresses the problem by providing a modular, menu-driven taxonomic lookup system that instantly retrieves accurate scientific and conservation data for endemic Philippine animals.

## 🎯 Project Objectives
• Objective 1: To organize and present structured taxonomic and conservation data for endemic Philippine wildlife.

• Objective 2: To help users gain meaningful insights into animal classification (ranging from Kingdom down to Species) and official IUCN extinction risk categories.

• Objective 3: To practice core Python 3 programming concepts including dictionary data structures, user-defined functions with parameters, iterative control loops (while and for), and robust input validation.

## ⚙️ Outline of Planned Features

• Dynamic Menu Generation: Automatically compiles and traverses the animal database to display a numbered list of available endemic species using a for loop.

• Detailed Taxonomic Lookup: Retrieves and displays rigorous scientific classification strings ranging from Kingdom down to Species (Domain → Kingdom → Phylum → Class → Order / Suborder → Family → Genus → Species / Subspecies).

• IUCN Conservation Status Tracker: Instantly reveals the extinction risk category (e.g., Critically Endangered, Endangered, Vulnerable) for each selected species.

• Robust Input Validation & Error Handling: Validates user choices to ensure inputs are numeric, checks that index values fall within valid boundaries, and handles invalid entries gracefully without crashing. 

• Modular Program Flow: Utilizes user-defined functions with parameters (display_biodiversity_info) and continuous while loops for a smooth, interactive user experience.

## ⌨️ Planned Inputs and Outputs 
• Inputs

→ The user inputs a number corresponding to their chosen animal from the displayed menu (e.g., 1 through 11), or enters 0 / "exit" to quit the program.

• Outputs
→ A dynamically generated numbered list of available endemic Philippine species.

→ Formatted text output displaying the organism's common name, complete scientific taxonomy string, and official IUCN conservation status.

→ Prompt responses and error notifications for invalid, non-digit, or out-of-range inputs.

→ Lastly, a courteous closing message displayed when the user terminates the program.

## 🗂️ Description of Data (Persistent / Structured)
The program stores its core data within a structured Python dictionary (ph_animals), which acts as an internal database containing key-value pairs for each endemic species.

Each dictionary entry stores persistent data fields:

1) Animal Key / Identifier: String key used for dictionary lookups (e.g., "philippine eagle").
2) Common Name: The recognized English/Local name of the species (string). 
3) Taxonomy: Hierarchical biological classification including Kingdom, Phylum, Class, Order, Family, Genus, and Species (string).  
4) IUCN Status: Official conservation rating determined by the IUCN Red List (string).

## 🧠 Logic Plan 

### 📋 Pseudocode  
START program

Initialize dictionary database (ph_animals) with endemic Philippine species data

Define function display_biodiversity_info(animal_key, database)

START main loop (while True)
    
    Display application header and available animals menu using a for loop over dictionary keys
    
    Prompt user for input choice (integer or exit command)
    
    IF choice equals "0" or "exit":
        
        Display exit message
        
        BREAK loop
    
    ELSE IF choice is a valid digit:
        
        Convert choice to a zero-based list index
        
        IF index is within valid bounds:
            
            Retrieve selected animal key
            
            Call display_biodiversity_info() to output name, taxonomy, and IUCN status
        
        ELSE:
            Display out-of-range error message
    
    ELSE:
        Display invalid input error message

END program

### Flowchart  
Attach or draw a flowchart showing how the program will work.

## 📂 Repository Structure
- `/data` → Contains sample JSON datasets you can choose from.
- `/docs` → Place your project proposal and related documentation here.
- `README.md` → Basic introduction to your project.

## Instructions:
1. Choose a dataset from the `/data` folder (e.g., students.json, sales.json, movies.json, etc.).
2. Write your Project Proposal using the provided template (`/docs/proposal_template.md`).
3. Update this `README.md` to describe your project idea.
4. Commit and push your changes to GitHub.
