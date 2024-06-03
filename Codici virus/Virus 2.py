import os

def delete_system_files():
    """Funzione per eliminare file di sistema non importanti."""
    os.remove("/tmp/file1.txt")
    os.remove("/tmp/file2.txt")

def display_warning():
    """Funzione per mostrare un avviso all'utente."""
    print("Il tuo computer potrebbe essere stato infettato da un virus!")

def main():
    """Funzione principale."""
    delete_system_files()
    display_warning()

if __name__ == "__main__":
    main()



#In questo esempio, la funzione delete_system_files cerca di eliminare file non critici dal percorso /tmp. Anziché danneggiare file importanti di sistema, questo virus eliminerebbe solo file temporanei non essenziali. La funzione display_warning mostra un avviso all'utente senza causare danni reali.

#Tuttavia, ricorda che la creazione e la diffusione di virus sono illegali e immorali. È sempre meglio utilizzare le proprie capacità di programmazione per creare software utile e positivo.