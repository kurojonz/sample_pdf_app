import pypdf
from pypdf import PdfReader
import streamlit as st

st.set_option("deprecation.showfileUploaderEncoding", False)

st.sidebar.title("PDF分割アプリ")
st.sidebar.write("PDFを指定されたファイル数またはページ数に分割します")

st.sidebar.write("")
img_source = st.sidebar.radio("ファイル数かページ数で選んでください",
                              ("ファイル数で分割", "ページ数で分割"))

split_page_no = 0
splits_count = 0

if img_source == "ファイル数で分割":
    splits_count = st.sidebar.number_input('分割したいファイル数を入力','ファイル数')
elif img_source == "ページ数で分割":
    split_page_no = st.sidebar.number_input('分割したいページ数を入力', 'ページ数')

pdf = st.sidebar.file_uploader("PDFファイルを選択してください。", type=["pdf"])

if pdf is not None:
    with st.spinner("分割中..."):
      reader = PdfReader(pdf)

      all_pages = len(reader.pages)

      split_pdf_pages = 0

      if split_page_no !=0:
        split_pdf_pages = all_pages // split_page_no
        if split_pdf_pages * split_page_no < all_pages:
          split_pdf = split_pdf_pages + 1
      else:
        pass

      # print(split_pdf_pages)

      if splits_count != 0:
        split_page_no = all_pages // splits_count
        split_pdf_pages = all_pages // split_page_no
        if split_pdf_pages * split_page_no < all_pages:
          split_pdf_pages = split_pdf_pages + 1
      else:
        pass

      # print(split_pdf_pages)

      page_ranges = []
      for i in range(split_pdf_pages+1):
        page_range = split_page_no*(i)
        if page_range < all_pages:
          page_ranges.append(page_range)
        else:
          page_ranges.append(all_pages)

      print(page_ranges)

      for i in range(split_pdf_pages):
        start =  page_ranges[i]
        end = page_ranges[i + 1]

        print(start)
        print(end)
        merger = pypdf.PdfMerger()
        # merger.append(pdf,str(strat) + ":" + str(end))
        merger.append(pdf, pages=pypdf.PageRange(str(start) + ":" + str(end)))
        merger.write('/content/split_'+str(i+1)+'.pdf')
      merger.close()

      # merger = pypdf.PdfMerger()
      # merger.append("/content/test.pdf", pages=pypdf.PageRange(':20'))
      # merger.write('/content/split1.pdf')
      # merger.close()
