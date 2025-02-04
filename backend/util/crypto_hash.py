import hashlib  # 📌 Βιβλιοθήκη που παρέχει διάφορους αλγορίθμους hashing, όπως SHA-256
import json  # 📌 Βιβλιοθήκη που επιτρέπει τη μετατροπή δομών δεδομένων σε JSON format

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    # 🔹 map(): Εφαρμόζει τη συνάρτηση json.dumps() σε κάθε στοιχείο της λίστας args
    # 🔹 json.dumps(): Μετατρέπει το κάθε δεδομένο (string, αριθμούς, λίστες κ.λπ.) σε JSON format (συμβολοσειρά)
    # 🔹 sorted(): Ταξινομεί τα JSON strings για να διασφαλιστεί η συνέπεια του hashing (ίδια δεδομένα -> ίδιο hash ανεξαρτήτως σειράς)
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    # 🔹 ''.join(): Συνενώνει όλα τα JSON strings σε μία μεγάλη συμβολοσειρά (string) χωρίς διαχωριστικό
    joined_data = ''.join(stringified_args)

    # 🔹 encode('utf-8'): Μετατρέπει τη συμβολοσειρά σε bytes (απαραίτητο για τον αλγόριθμο SHA-256)
    # 🔹 hashlib.sha256(): Δημιουργεί ένα SHA-256 hash από τα bytes της συμβολοσειράς
    # 🔹 hexdigest(): Μετατρέπει το αποτέλεσμα σε δεκαεξαδικό string για ευκολότερη ανάγνωση
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    # 📌 Δοκιμή της συνάρτησης με διαφορετική σειρά εισόδου για να ελέγξουμε αν παράγει το ίδιο hash
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")  
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")  

# 🔹 __name__: Μια ειδική μεταβλητή που δείχνει αν το script εκτελείται απευθείας ή αν έχει εισαχθεί ως module
# 🔹 __main__: Αν το script εκτελείται απευθείας (και όχι ως module), τότε εκτελείται η main()
if __name__ == '__main__':
    main()
