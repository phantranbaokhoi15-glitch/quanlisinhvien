import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Tạo dữ liệu từ danh sách 10 sinh viên
data = {
    "Họ và tên": [
        "Phan Trần Bảo Khôi",
        "Lương Minh Tuấn",
        "Nguyễn Quang Tiến",
        "Lê An Bảo Ngọc",
        "Nguyễn Hữu Chiến",
        "Đinh Thị Quỳnh Như",
        "Nguyễn Thị Phương Trâm",
        "Nguyễn Đình Quốc",
        "Dương Quốc Khang",
        "Nguyễn Anh Kiệt",
    ],
    "Chuyên cần": [9, 8, 10, 10, 8, 9, 6, 10, 7, 9],
    "Giữa kỳ": [8, 7, 9, 9, 7.5, 8.5, 5, 9, 6.5, 8],
    "Cuối kỳ": [8.5, 7.5, 9, 8.5, 8, 9, 5.5, 9.5, 7, 8.5],
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết (Chuyên cần 20%, Giữa kỳ 30%, Cuối kỳ 50%)
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"] + 0.3 * df["Giữa kỳ"] + 0.5 * df["Cuối kỳ"]
).round(2)


# 3. Xếp loại sinh viên
def xep_loai(diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >= 7.0:
    return "Khá"
  elif diem >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Hiển thị bảng điểm trên Web App
st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 4. Thống kê cơ bản
st.subheader("Thống kê chung của lớp")
dtb_lop = df["Tổng kết"].mean().round(2)
max_sv = df.loc[df["Tổng kết"].idxmax()]
min_sv = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = len(df[df["Tổng kết"] >= 5])

st.write(f"- **Điểm tổng kết trung bình của lớp:** {dtb_lop}")
st.write(
    f"- **Sinh viên có điểm tổng kết cao nhất:** **{max_sv['Họ và tên']}**"
    f" ({max_sv['Tổng kết']} điểm)"
)
st.write(
    f"- **Sinh viên có điểm tổng kết thấp nhất:** **{min_sv['Họ và tên']}**"
    f" ({min_sv['Tổng kết']} điểm)"
)
st.write(f"- **Số sinh viên đạt (điểm tổng kết >= 5):** {so_sv_dat} sinh viên")

# 5. Danh sách chọn sinh viên để xem chi tiết
st.subheader("Tra cứu thông tin cá nhân sinh viên")
selected_name = st.selectbox("Chọn sinh viên cần xem:", df["Họ và tên"])
student_info = df[df["Họ và tên"] == selected_name].iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Điểm Chuyên cần", student_info["Chuyên cần"])
col2.metric("Điểm Giữa kỳ", student_info["Giữa kỳ"])
col3.metric("Điểm Cuối kỳ", student_info["Cuối kỳ"])

st.info(
    f"**Điểm tổng kết:** {student_info['Tổng kết']} | **Xếp loại:**"
    f" {student_info['Xếp loại']}"
)

# 6. Trực quan hóa biểu đồ cột điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ và tên"], df["Tổng kết"], color="#4C72B0")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_title("Biểu đồ điểm tổng kết")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# Thông tin người tạo ở cuối trang (chữ nhỏ)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>Người tạo:"
    " [Phan Trần Bảo Khôi] - MSSV: [060208005632]</p>",
    unsafe_allow_html=True,
)
