# HCMC-AIC2024
https://aichallenge.hochiminhcity.gov.vn/

## Directory Structure

### Back-end side

```
# ./backend
/controller         # định nghĩa logic
/db                 # database: lưu trữ các .bin file của FAISS, ...
/src                # định nghĩa các core-class
    /tools          # định nghĩa các công cụ
    /processor      # định nghĩa các hàm tiền/hậu xử lý ảnh, chữ, ...
    helpers.py      # định nghĩa các hàm trợ giúp như đọc file, chuyển định dạng, ...
/routes
app.py

```