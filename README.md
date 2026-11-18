# Computer Science 2

## Philippine Biodiversity Taxonomic Finder 
(with IUCN Conservation Status Integration)

## → Project Description
The Philippine Biodiversity Taxonomic Finder is an interactive Python 3 console application designed to help students, researchers, and nature enthusiasts explore endemic Philippine wildlife. The program allows users to select an animal from an organized menu, view its complete scientific classification (taxonomy), and check its official International Union for Conservation of Nature (IUCN) conservation status.

## → Problem Statement
Many students and wildlife advocates lack a centralized, quick-access digital tool to look up structured scientific information—such as hierarchical taxonomy and extinction risk—specifically tailored to endemic Philippine biodiversity. Scattered data sources make learning about local endangered species inefficient. This program addresses the problem by providing a modular, menu-driven taxonomic lookup system that instantly retrieves accurate scientific and conservation data for endemic Philippine animals.

## → Outline of Features

• Dynamic Menu Generation: Automatically compiles and traverses the animal database to display a numbered list of available endemic species using a for loop.

• Detailed Taxonomic Lookup: Retrieves and displays rigorous scientific classification strings ranging from Kingdom down to Species (Domain → Kingdom → Phylum → Class → Order / Suborder → Family → Genus → Species / Subspecies).

• IUCN Conservation Status Tracker: Instantly reveals the extinction risk category (e.g., Critically Endangered, Endangered, Vulnerable) for each selected species.

• Robust Input Validation & Error Handling: Validates user choices to ensure inputs are numeric, checks that index values fall within valid boundaries, and handles invalid entries gracefully without crashing. 

• Modular Program Flow: Utilizes user-defined functions with parameters (display_biodiversity_info) and continuous while loops for a smooth, interactive user experience.

## Description of Data (Persistent / Structured)
The application stores its core data within a structured Python dictionary (ph_animals), which acts as an internal database containing key-value pairs for each endemic species.

Each dictionary entry stores persistent data fields:

1) Animal Key / Identifier: String key used for dictionary lookups (e.g., "philippine eagle").
2) Common Name: The recognized English/Local name of the species (string). 
3) Taxonomy: Hierarchical biological classification including Kingdom, Phylum, Class, Order, Family, Genus, and Species (string).  
4) IUCN Status: Official conservation rating determined by the IUCN Red List (string). 

## 📂 Repository Structure
- `/data` → Contains sample JSON datasets you can choose from.
- `/docs` → Place your project proposal and related documentation here.
- `README.md` → Basic introduction to your project.

## Instructions:
1. Choose a dataset from the `/data` folder (e.g., students.json, sales.json, movies.json, etc.).
2. Write your Project Proposal using the provided template (`/docs/proposal_template.md`).
3. Update this `README.md` to describe your project idea.
4. Commit and push your changes to GitHub.
