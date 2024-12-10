import streamlit as st
def main():
    # Judul
    st.balloons()
    st.snow()
    
    st.title("Kalkulator Sederhana")
    st.write("Aplikasi ini menghitung operasi dasar matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.")
    # Input angka pertama
    num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)

    # Input angka kedua
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)
    
    # Pilihan operasi
    operation = st.selectbox(
        "Pilih operasi matematika:",
        ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian")
    )
    
    # Tombol untuk menghitung
    if st.button("Hitung"):
        if operation == "Penjumlahan":
            result = num1 + num2
            st.success(f"Hasil Penjumlahan: {result}",icon=":material/thumb_up:")
        elif operation == "Pengurangan":
            result = num1 - num2
            st.success(f"Hasil Pengurangan: {result}",icon=":material/thumb_up:")
        elif operation == "Perkalian":
            result = num1 * num2
            st.success(f"Hasil Perkalian: {result}",icon=":material/thumb_up:")
        elif operation == "Pembagian":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Hasil Pembagian: {result}",icon=":material/thumb_up:")
            else:
                st.warning('Kesalahan: Pembagian dengan nol tidak diperbolehkan.', icon="⚠️")
    
if __name__ == "__main__":
    main()
  
