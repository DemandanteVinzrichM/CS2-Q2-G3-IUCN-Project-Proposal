"""
Project Proposal: Philippine Biodiversity Taxonomic Finder
Computer Science 2 - Q2 to Q4 - Group 3
"""

# --- DATABASE SECTION ---
# Storing our Philippine endemic animals, their taxonomy, and IUCN status
ph_animals = {
    "philippine eagle": {
        "name": "Philippine Eagle",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Aves | Order: Accipitriformes | Family: Accipitridae | Genus: Pithecophaga | Species: P. jefferyi",
        "iucn": "Critically Endangered (CR)",
    },
    "philippine tarsier": {
        "name": "Philippine Tarsier",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Mammalia | Order: Primates | Family: Tarsiidae | Genus: Carlito | Species: C. syrichta",
        "iucn": "Near Threatened (NT)",
    },
    "tamaraw": {
        "name": "Tamaraw",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Mammalia | Order: Artiodactyla | Family: Bovidae | Genus: Bubalus | Species: B. mindorensis",
        "iucn": "Critically Endangered (CR)",
    },
    "palawan mouse-deer": {
        "name": "Palawan Mouse-Deer",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Mammalia | Order: Artiodactyla | Family: Tragulidae | Genus: Tragulus | Species: T. nigricans",
        "iucn": "Endangered (EN)",
    },
    "visayan warty pig": {
        "name": "Visayan Warty Pig",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Mammalia | Order: Artiodactyla | Family: Suidae | Genus: Sus | Species: S. cebifrons",
        "iucn": "Critically Endangered (CR)",
    },
    "philippine crocodile": {
        "name": "Philippine Crocodile",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Reptilia | Order: Crocodilia | Family: Crocodylidae | Genus: Crocodylus | Species: C. mindorensis",
        "iucn": "Critically Endangered (CR)",
    },
    "rufous hornbill": {
        "name": "Rufous Hornbill",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Aves | Order: Bucerotiformes | Family: Bucerotidae | Genus: Buceros | Species: B. hydrocorax",
        "iucn": "Vulnerable (VU)",
    },
    "palawan peacock-pheasant": {
        "name": "Palawan Peacock-Pheasant",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Aves | Order: Galliformes | Family: Phasianidae | Genus: Polyplectron | Species: P. napoleonis",
        "iucn": "Vulnerable (VU)",
    },
    "palawan binturong": {
        "name": "Palawan Binturong",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Mammalia | Order: Carnivora | Family: Viverridae | Genus: Arctictis | Species: A. binturong (Subspecies: A. b. whitei)", 
        "iucn" : "Vulnerable (VU)",
    },
    "negros bleeding-heart": {
        "name": "Negros Bleeding-heart Pigeon",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Aves | Order: Columbiformes | Family: Columbidae | Genus: Gallicolumba | Species: G. keayi",
        "iucn": "Critically Endangered (CR)",
    },
    "calamian deer": {
        "name": "Calamian Deer",
        "taxonomy": "Kingdom: Animalia | Phylum: Chordata | Class: Mammalia | Order: Artiodactyla | Family: Cervidae | Genus: Axis | Species: A. calamianensis",
        "iucn": "Endangered (EN)",
    },
}


# --- FUNCTION SECTION ---
# This function uses parameters to display the taxonomy and IUCN status neatly po
def display_biodiversity_info(animal_key, database):
    animal_data = database[animal_key]
    print("\n" + "=" * 50)
    print(f"ANIMAL: {animal_data['name']}")
    print(f"TAXONOMY: {animal_data['taxonomy']}")
    print(f"IUCN CONSERVATION STATUS: {animal_data['iucn']}")
    print("=" * 50 + "\n")


# --- MAIN PROGRAM LOOP ---
def main():
    print("--- Philippine Biodiversity Taxonomic Finder, with International Union for Conservation of Nature (IUCN) Basis ---")

    while True:
        print("\nAvailable Animals to Choose From:")

        # Convert dictionary keys into a list for numbering
        animal_keys = list(ph_animals.keys())

        # A "for" loop to display the menu options
        for i in range(len(animal_keys)):
            key = animal_keys[i]
            display_name = ph_animals[key]["name"]
            print(f"[{i + 1}] {display_name}")

        print("[0] Exit Program")

        # Asking the user for input
        choice = (
            input("\nKindly enter the number of your chosen animal: ").strip().lower()
        )

        # Exit condition
        if choice == "0" or choice == "exit":
            print("\nThank you for exploring Philippine wildlife with us po!")
            break

        # Validating the user's numeric input
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(animal_keys):
                selected_key = animal_keys[index]
                display_biodiversity_info(selected_key, ph_animals)
            else:
                print(
                    "\nError: Number is out of range. Please choose from the list po."
                )
        else:
            print("\nError: Invalid input. Please enter a valid number from the menu.")


# Running the main program loop
if __name__ == "__main__":
    main()
