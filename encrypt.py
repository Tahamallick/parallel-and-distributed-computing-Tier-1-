from cryptography.fernet import Fernet
import os


# Generate a key for encryption (you can save this key securely for decryption)
def generate_key():
    return Fernet.generate_key()


# Save the encryption key to a file (You should keep this key secure)
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# Load the encryption key from the file
def load_key():
    return open("secret.key", "rb").read()


# Encrypt a file
def encrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)


# Decrypt a file
def decrypt_file(file_name, key):
    f = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    # Write the decrypted data back to a new CSV file
    with open(file_name.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)


# Encrypt all CSV files in the 'data' folder
def encrypt_data_in_folder():
    key = generate_key()  # Generate a key for encryption
    save_key(key)  # Save the key to a file (keep this key secure for decryption)

    data_folder = "data"  # Your folder containing CSV files

    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):  # Check if the file is a CSV
            file_path = os.path.join(data_folder, filename)
            encrypt_file(file_path, key)
            print(f"Encrypted {filename}.")


# Decrypt all encrypted CSV files in the 'data' folder
def decrypt_data_in_folder():
    key = load_key()  # Load the key used for encryption

    data_folder = "data"  # Your folder containing encrypted files

    for filename in os.listdir(data_folder):
        if filename.endswith(".csv.encrypted"):  # Check if the file is encrypted
            file_path = os.path.join(data_folder, filename)
            decrypt_file(file_path, key)
            print(f"Decrypted {filename}.")


# Run the encryption or decryption
if __name__ == "__main__":
    encrypt: encrypt_data_in_folder()
    #decrypt: decrypt_data_in_folder()
    pass
