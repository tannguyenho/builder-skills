# Quy trình Agent Kiểm chứng (Verification Agent Protocol)

Sau khi tổng hợp xong, tạo một **Agent Kiểm chứng (V1)** để rà soát mọi sản phẩm về độ nhất quán, độ chính xác và độ đầy đủ. Bước này bắt được những vấn đề mà từng agent riêng lẻ và bước tổng hợp có thể bỏ sót.

## Khi nào chạy

- Sau khi tổng hợp xong và mọi file sản phẩm đã được ghi
- Trước khi trình bày đầu ra cuối cùng cho user
- Dùng một agent: **V1: Kiểm chứng (Verification)**

## Nhiệm vụ của agent

Agent V1 đọc TẤT CẢ file sản phẩm (không phải file thô) và đối chiếu chúng với các quy tắc bên dưới. Agent tạo ra file `verification-report.md` trong thư mục project.

## Kiểm tra chung

Áp dụng cho mọi skill nghiên cứu sản phẩm trong plugin:

### 1. Nhận định không có nguồn
Mọi nhận định định lượng phải có nhãn dữ liệu: **[Data]**, **[Estimate]**, **[Assumption]**, hoặc **[Opinion]**. Đánh dấu mọi con số, tỷ lệ phần trăm hay khẳng định về dữ kiện không có nhãn.

### 2. Mâu thuẫn nội bộ
Đối chiếu chéo con số và phát biểu giữa các file sản phẩm. Đánh dấu khi:
- Cùng một chỉ số xuất hiện với giá trị khác nhau ở hai file
- Một nhận định ở file này mâu thuẫn với một nhận định ở file khác
- Mức tin cậy không khớp nhau (vd "Độ tin cậy Cao" ở một file, trong khi dữ liệu khác ở file khác cho thấy chỉ nên là Trung bình)

### 3. Độ nhất quán của mức tin cậy
Xác minh mức tin cậy khớp với bằng chứng:
- Một nhận định chỉ có một nguồn Tier 3 không thể được chấm **Cao**
- Một nhận định có nhiều nguồn Tier 1 không nên bị chấm **Thấp**
- Mọi mục lớn đều phải có mức tin cậy

### 4. Đã khai báo chỗ thiếu dữ liệu
Mọi sản phẩm phải có mục Chỗ thiếu dữ liệu. Đánh dấu:
- File thiếu hẳn mục Chỗ thiếu dữ liệu
- Mục mà dữ liệu rõ ràng mỏng nhưng không khai báo chỗ thiếu
- Chỗ thiếu được nêu trong file thô nhưng không được đưa vào sản phẩm tổng hợp

### 5. Có flag
Mọi sản phẩm phải kết thúc bằng mục Red Flags và Yellow Flags. Đánh dấu:
- File thiếu các mục này
- File ghi "Không phát hiện flag nào" trong khi nội dung rõ ràng có rủi ro

### 6. Dữ liệu cũ
Đánh dấu mọi điểm dữ liệu cũ hơn 18 tháng mà không được ghi chú là có thể đã lỗi thời.

### 7. Trùng nguồn
Đánh dấu khi cùng một nguồn được dùng làm "đối chiếu độc lập" ở nhiều chỗ. Hai nhận định cùng trích một bài blog thì không có kiểm chứng độc lập.

## Kiểm tra riêng: product-competitors

Ngoài các kiểm tra chung ở trên, xác minh thêm:

### Battle card nhất quán với báo cáo
- Mọi đối thủ trong battle card phải có trong bảng Tổng quan các người chơi chính của `competitors-report.md`
- Điểm mạnh/điểm yếu trong battle card không được mâu thuẫn với hồ sơ đối thủ trong báo cáo
- Mức đe doạ phải nhất quán giữa battle card và báo cáo

### Ma trận khớp với hồ sơ
- Mọi đối thủ trong `competitive-matrix.md` phải có hồ sơ trong `competitors-report.md`
- Đánh giá tính năng (Mạnh/Đạt/Yếu/Không có) trong ma trận phải có bằng chứng hỗ trợ trong báo cáo hoặc battle card
- Các mục trong phân tích khoảng trống phải gắn với phát hiện thật, không phải giả định

### Bức tranh giá nhất quán với hồ sơ
- Dữ liệu giá trong `pricing-landscape.md` phải khớp với giá được nêu trong battle card
- Value metric phải nhất quán giữa bức tranh giá và hồ sơ đối thủ
- Đánh giá chi phí chuyển đổi phải khớp giữa bức tranh giá và battle card

### Độ ăn khớp giữa các sản phẩm
- Cơ hội chiến lược trong báo cáo phải được hỗ trợ bởi bằng chứng từ ít nhất hai sản phẩm (vd khoảng trống giá + phàn nàn của khách hàng)
- Rủi ro chiến lược phải truy được về dữ liệu cụ thể của đối thủ
- Đánh giá moat phải nhắc tới đối thủ và bằng chứng cụ thể

## Đầu ra: verification-report.md

```markdown
# Báo cáo kiểm chứng: {project-name}
*Ngày tạo: {date}*

## Tóm tắt
- **Vấn đề nghiêm trọng (Critical):** {count}
- **Cảnh báo (Warnings):** {count}
- **Thông tin (Info):** {count}

## Vấn đề nghiêm trọng
Những vấn đề có thể làm sai lệch việc ra quyết định. Quy trình dừng ở đây để user xem xét.

### {Tiêu đề vấn đề}
- **File:** {các file bị ảnh hưởng}
- **Mục:** {tên mục}
- **Vấn đề:** {mô tả}
- **Đề xuất sửa:** {cách giải quyết}

## Cảnh báo
Những vấn đề làm giảm chất lượng nhưng không chặn việc ra quyết định.

### {Tiêu đề vấn đề}
- **File:** {các file bị ảnh hưởng}
- **Vấn đề:** {mô tả}
- **Đề xuất sửa:** {cách giải quyết}

## Thông tin
Cải thiện nhỏ và quan sát.

- {quan sát}
- {quan sát}

## Checklist kiểm chứng
- [ ] Mọi nhận định định lượng đã gắn nhãn
- [ ] Không phát hiện mâu thuẫn nội bộ
- [ ] Mức tin cậy nhất quán với bằng chứng
- [ ] Mọi sản phẩm đã khai báo chỗ thiếu dữ liệu
- [ ] Mọi sản phẩm có Red/Yellow Flags
- [ ] Không có dữ liệu cũ chưa được đánh dấu
- [ ] Không có đối chiếu giả do trùng nguồn
- [ ] Battle card nhất quán với báo cáo (riêng skill)
- [ ] Ma trận khớp với hồ sơ (riêng skill)
- [ ] Bức tranh giá nhất quán với hồ sơ (riêng skill)
- [ ] Cơ hội có bằng chứng từ nhiều nguồn (riêng skill)
```

## Điều khiển luồng

- **Nếu số vấn đề Nghiêm trọng > 0:** Dừng lại. Báo user: "Kiểm chứng phát hiện {N} vấn đề nghiêm trọng có thể ảnh hưởng tới việc ra quyết định." Liệt kê chúng. Hỏi: "Mình có nên sửa những điểm này trước khi tiếp tục, hay cứ tiếp tục như hiện tại?"
- **Nếu chỉ có Cảnh báo/Thông tin:** Hiển thị tóm tắt một dòng: "Kiểm chứng xong: {N} cảnh báo, {N} mục thông tin. Xem chi tiết trong `verification-report.md`." Tiếp tục.
