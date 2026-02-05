import sys
import requests
import urllib3
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print("Usage: url file")
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    r = s.get(url, verify=False)
    res = r.text
    if r.status_code == 200:
        print('sudah ke download')
        decode = base64.b64decode(res)
        with open('result.png', 'wb') as f:
            f.write(decode)
            print('berhasil bikin file')
        # Menggunakan OCR untuk membaca teks dalam gambar
        try: 
            from PIL import Image
            import pytesseract
            
            # OCR
            text = pytesseract.image_to_string(Image.open('result.png'))
            
            # Ambil baris ke-9 (sesuaikan index jika perlu)
            lines = text.splitlines()
            if len(lines) > 9:
                target_hex = lines[9].replace(" ", "").strip()
                print(f"\nHex ditemukan: {target_hex}")
                
                # Decode Hex
                flag = bytes.fromhex(target_hex).decode('utf-8')
                print(f"Flag: {flag}")
            else:
                print("Baris ke-9 tidak ditemukan.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    else:
        print('belum ke download')

if __name__ == '__main__':
    main()