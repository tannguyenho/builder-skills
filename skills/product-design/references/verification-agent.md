# Quy trình của agent kiểm chứng (Verification Agent Protocol)

Sau khi tổng hợp xong, tạo một **agent kiểm chứng (V1)** để rà soát mọi sản phẩm bàn giao về độ nhất quán, chính xác và đầy đủ. Bước này bắt những vấn đề mà từng agent riêng lẻ và bước tổng hợp có thể bỏ sót.

## Khi nào chạy

- Sau khi tổng hợp xong và mọi file bàn giao đã được viết
- Trước khi phase tiếp theo bắt đầu (vd trước Phase 3.5 Research Gate trong product-design)
- Dùng một agent: **V1: Verification**

## Nhiệm vụ của agent

Agent V1 đọc TẤT CẢ file bàn giao (không phải file thô) và đối chiếu với các quy tắc bên dưới. Nó tạo ra `verification-report.md` trong thư mục dự án.

## Kiểm tra chung

Áp dụng cho mọi skill trong plugin:

### 1. Khẳng định không có nguồn
Mọi khẳng định định lượng phải có nhãn dữ liệu: **[Data]**, **[Estimate]**, **[Assumption]**, hoặc **[Opinion]**. Gắn cờ mọi con số, tỉ lệ phần trăm, hay khẳng định sự kiện không có nhãn.

### 2. Mâu thuẫn nội bộ
Đối chiếu chéo con số và phát biểu giữa các file bàn giao. Gắn cờ khi:
- Cùng một chỉ số xuất hiện với giá trị khác nhau ở hai file
- Một khẳng định ở file này mâu thuẫn với khẳng định ở file khác
- Mức độ tin cậy không khớp (vd "Độ tin cậy cao" ở một file, trong khi dữ liệu khác ở file khác cho thấy chỉ là Trung bình)

### 3. Độ nhất quán của mức độ tin cậy
Xác minh rằng mức độ tin cậy khớp với bằng chứng:
- Một khẳng định chỉ có một nguồn Tier 3 không thể được xếp **Cao**
- Một khẳng định có nhiều nguồn Tier 1 không nên bị xếp **Thấp**
- Mọi mục chính phải có mức độ tin cậy

### 4. Khai báo khoảng trống dữ liệu
Mọi sản phẩm bàn giao phải có mục Khoảng trống dữ liệu (Data Gaps). Gắn cờ:
- File thiếu hẳn mục Khoảng trống dữ liệu
- Các mục mà dữ liệu rõ ràng mỏng nhưng không khai báo khoảng trống
- Khoảng trống được nhắc trong file thô nhưng không được đưa vào sản phẩm bàn giao đã tổng hợp

### 5. Có cờ cảnh báo
Mọi sản phẩm bàn giao phải kết thúc bằng mục Cờ đỏ và Cờ vàng. Gắn cờ:
- File thiếu các mục này
- File ghi "Không phát hiện cờ nào" trong khi nội dung rõ ràng có rủi ro

### 6. Dữ liệu cũ
Gắn cờ mọi điểm dữ liệu cũ hơn 18 tháng mà không được đánh dấu là có thể đã lỗi thời.

### 7. Trùng nguồn
Gắn cờ khi cùng một nguồn được dùng làm "xác nhận độc lập" ở nhiều chỗ. Hai khẳng định cùng trích một bài blog thì không có kiểm chứng độc lập.

## Kiểm tra riêng của skill: product-design

Ngoài các kiểm tra chung ở trên, xác minh thêm:

### Nhất quán giữa các phase
- **Chiến lược phản ánh dữ liệu thị trường:** Lean Canvas, định vị và GTM ở Phase 4 có tham chiếu phát hiện cụ thể từ Phase 3 không? Gắn cờ các khẳng định chiến lược không có nghiên cứu hậu thuẫn.
- **Sản phẩm phản ánh nỗi đau khách hàng:** Định nghĩa MVP (Phase 6) có giải quyết các nỗi đau hàng đầu được xác định trong `target-audience.md` không? Gắn cờ các tính năng không ánh xạ tới nhu cầu khách hàng nào đã được thẩm định.
- **Tài chính phản ánh mô hình kinh doanh:** Dự phóng doanh thu (Phase 7) có dùng giá và unit economics từ `market-analysis.md` và `business-model.md` không? Gắn cờ các giả định dự phóng mâu thuẫn với dữ liệu nghiên cứu.
- **Thẩm định bao phủ rủi ro chính:** Phân tích rủi ro (Phase 8) có xử lý các Cờ đỏ và khoảng trống dữ liệu đã nêu ở các phase trước không? Gắn cờ các rủi ro đã được xác định trong nghiên cứu nhưng vắng mặt ở phần thẩm định.

### Nhất quán về số liệu
- Các con số TAM/SAM/SOM phải nhất quán giữa `market-analysis.md`, `lean-canvas.md` và `revenue-model.md`
- Các tham chiếu về giá phải khớp giữa `competitor-landscape.md` và `business-model.md`
- Mô tả phân khúc khách hàng phải nhất quán giữa `target-audience.md`, `lean-canvas.md` và `mvp-definition.md`

## Đầu ra: verification-report.md

```markdown
# Báo cáo kiểm chứng: {project-name}
*Tạo lúc: {date}*

## Tóm tắt
- **Vấn đề nghiêm trọng (Critical):** {số lượng}
- **Cảnh báo (Warning):** {số lượng}
- **Thông tin (Info):** {số lượng}

## Vấn đề nghiêm trọng
Những vấn đề có thể làm sai lệch việc ra quyết định. Quy trình dừng ở đây để user xem xét.

### {Tiêu đề vấn đề}
- **File:** {các file bị ảnh hưởng}
- **Mục:** {tên mục}
- **Vấn đề:** {mô tả}
- **Đề xuất sửa:** {cách xử lý}

## Cảnh báo
Những vấn đề làm giảm chất lượng nhưng không chặn việc ra quyết định.

### {Tiêu đề vấn đề}
- **File:** {các file bị ảnh hưởng}
- **Vấn đề:** {mô tả}
- **Đề xuất sửa:** {cách xử lý}

## Thông tin
Cải thiện nhỏ và nhận xét.

- {nhận xét}
- {nhận xét}

## Checklist kiểm chứng
- [ ] Mọi khẳng định định lượng đều có nhãn
- [ ] Không phát hiện mâu thuẫn nội bộ
- [ ] Mức độ tin cậy nhất quán với bằng chứng
- [ ] Mọi sản phẩm bàn giao đều khai báo khoảng trống dữ liệu
- [ ] Mọi sản phẩm bàn giao đều có Cờ đỏ/Cờ vàng
- [ ] Không có dữ liệu cũ chưa được đánh dấu
- [ ] Không có xác nhận giả do trùng nguồn
- [ ] Chiến lược phản ánh dữ liệu thị trường (giữa các phase)
- [ ] Sản phẩm phản ánh nỗi đau khách hàng (giữa các phase)
- [ ] Tài chính phản ánh mô hình kinh doanh (giữa các phase)
- [ ] Thẩm định bao phủ các rủi ro đã xác định (giữa các phase)
```

## Điều khiển luồng

- **Nếu số vấn đề Critical > 0:** Dừng lại. Hiển thị cho user: "Bước kiểm chứng phát hiện {N} vấn đề nghiêm trọng có thể ảnh hưởng tới việc ra quyết định." Liệt kê chúng. Hỏi: "Mình sửa những vấn đề này trước khi đi tiếp, hay cứ đi tiếp như hiện tại?"
- **Nếu chỉ có Warning/Info:** Hiển thị tóm tắt một dòng: "Kiểm chứng xong: {N} cảnh báo, {N} mục thông tin. Xem `verification-report.md` để biết chi tiết." Đi tiếp sang phase sau.
