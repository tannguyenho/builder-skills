# Đợt 2: Khai thác cảm nhận khách hàng

Đọc `research-principles.md` trước.

---

## Agent B1: Khai thác review (Review Mining)

```
Nhiệm vụ nghiên cứu: Khai thác review của khách hàng về các đối thủ trong {product category}
Bối cảnh: {tóm tắt sản phẩm từ intake}
Đối thủ cần phân tích: {danh sách từ Đợt A}

Khai thác review cho thấy khách hàng thật sự trải nghiệm gì — không phải những gì marketing của đối thủ hứa hẹn. Khoảng cách giữa lời hứa và thực tế chính là nơi cơ hội nằm.

XỬ LÝ KHI REVIEW KHAN HIẾM:
Một số thị trường (đặc biệt B2B, ngách, hoặc nhóm sản phẩm mới nổi) có rất ít review chính thức trên G2/Capterra. Khi đó:
1. Mở rộng sang nền tảng khác: App Store, Play Store, Trustpilot, review trên Google Maps (cho sản phẩm/dịch vụ vật lý), các trang review chuyên ngành
2. Tìm case study và lời chứng thực (testimonial) trên website đối thủ — rút ra ngôn ngữ được dùng
3. Tìm "{competitor name} experience" hoặc "{competitor name} honest review" trên blog và YouTube
4. Dựa nhiều hơn vào khai thác diễn đàn (Đợt B2) để lấy ý kiến không qua chọn lọc
5. Khai báo rõ sự khan hiếm trong mục Chỗ thiếu dữ liệu — "chỉ tìm được X review trên các nền tảng" bản thân đã là thông tin có giá trị (nó báo hiệu thị trường còn non hoặc ít người chuyển đổi)
Luôn kèm ít nhất 2-3 trích dẫn nguyên văn cho mỗi đối thủ, kể cả khi chúng đến từ bài blog, tweet hay bình luận diễn đàn chứ không phải nền tảng review chính thức.

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Nền tảng review tổng hợp (2 lượt tìm cho mỗi đối thủ):
- "{competitor name} reviews G2"
- "{competitor name} reviews Capterra" OR "Trustradius"
- "{competitor name} reviews Product Hunt"
- "{competitor name} app store reviews" (nếu là sản phẩm mobile)

VÒNG 2 — Đào sâu review tiêu cực (1-2 lượt tìm cho mỗi đối thủ):
- "{competitor name} complaints"
- "{competitor name} problems reddit"
- "{competitor name} worst things"

VÒNG 3 — Mẫu yêu cầu tính năng (1-2 lượt tìm):
- "{competitor name} feature request"
- "{competitor name} missing features"
- "{product category} wishlist"

Với MỖI đối thủ, rút ra:

## {Tên đối thủ} — Phân tích review

### Số lượng review & điểm đánh giá
- **G2:** {count} review, {avg} sao
- **Capterra:** {count} review, {avg} sao
- **TrustRadius:** {count} review, {avg} sao
- **Product Hunt:** {upvotes}, {sắc thái bình luận}
- **App Store / Play Store:** {nếu có}

### Điều người dùng thích (3-5 chủ đề hàng đầu)
Với mỗi chủ đề:
- **Chủ đề:** {vd "Onboarding dễ"}
- **Tần suất:** được nhắc trong ~{X}% review tích cực
- **Trích dẫn nguyên văn:**
  - "{trích dẫn chính xác}" — {nguồn, ngày}
  - "{trích dẫn chính xác}" — {nguồn, ngày}

### Điều người dùng ghét (3-5 chủ đề hàng đầu)
Với mỗi chủ đề:
- **Chủ đề:** {vd "Giá thấy bất hợp lý khi dùng nhiều"}
- **Tần suất:** được nhắc trong ~{X}% review tiêu cực
- **Mức nghiêm trọng:** gây khó chịu / gây cản trở / khiến bỏ hẳn (deal-breaker)
- **Trích dẫn nguyên văn:**
  - "{trích dẫn chính xác}" — {nguồn, ngày}
  - "{trích dẫn chính xác}" — {nguồn, ngày}

### Tính năng được yêu cầu nhiều nhất
- {tính năng 1} — được nhắc {X} lần
- {tính năng 2} — được nhắc {X} lần
- {tính năng 3} — được nhắc {X} lần

### Tín hiệu rời bỏ
Lý do người dùng rời bỏ đối thủ này:
- {lý do 1 — kèm bằng chứng}
- {lý do 2 — kèm bằng chứng}
- {lý do 3 — kèm bằng chứng}

---

Sau tất cả đối thủ:

## Mẫu nỗi đau chung giữa các đối thủ
| Chủ đề nỗi đau | {Đối thủ 1} | {Đối thủ 2} | {Đối thủ 3} | {Đối thủ 4} | Cơ hội |
|-----------|----------|----------|----------|----------|-------------|
| {nỗi đau 1} | mức nghiêm trọng | mức nghiêm trọng | mức nghiêm trọng | mức nghiêm trọng | {hàm ý} |
| {nỗi đau 2} | ... | ... | ... | ... | ... |

Nỗi đau chung của nhiều đối thủ = vấn đề mang tính cấu trúc của thị trường = cơ hội lớn nhất.

## Chỗ thiếu dữ liệu
- [Đối thủ có ít review]
- [Nền tảng chưa kiểm tra]

Lưu vào: {project-name}/raw/review-mining.md
```

---

## Agent B2: Khai thác diễn đàn & cộng đồng (Forum & Community Mining)

```
Nhiệm vụ nghiên cứu: Khai thác diễn đàn và cộng đồng để lấy tiếng nói khách hàng về {product category}
Bối cảnh: {tóm tắt sản phẩm từ intake}
Đối thủ: {danh sách từ Đợt A}

Khai thác diễn đàn bắt được những ý kiến không qua chọn lọc mà người ta sẽ không viết trong review chính thức. Nó cũng cho thấy đúng ngôn ngữ khách hàng dùng — mỏ vàng cho định vị và viết copy.

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Reddit (3-4 lượt tìm):
- "site:reddit.com {product category} recommendations"
- "site:reddit.com {competitor name} alternative"
- "site:reddit.com {problem statement} tool"
- "site:reddit.com switching from {competitor name}"

VÒNG 2 — Cộng đồng indie (2-3 lượt tìm):
- "site:indiehackers.com {product category}"
- "site:news.ycombinator.com {product category}"
- "{product category} forum discussion"

VÒNG 3 — Hỏi đáp và cộng đồng ngách (2 lượt tìm):
- "site:quora.com best {product category}"
- "{product category} community Slack Discord"

VÒNG 4 — Câu chuyện chuyển đổi (1-2 lượt tìm):
- "switched from {competitor name} to"
- "migrating from {competitor name}"
- "why I left {competitor name}"

TUỲ CHỌN — Gói dữ liệu mạng xã hội do user cung cấp:
Nếu user đã có sẵn một bản export từ mạng xã hội (X/Twitter, nhóm Facebook,
TikTok, Threads, diễn đàn…): bài đăng, thread trả lời, kết quả tìm kiếm, bản tóm
tắt tài khoản hoặc báo cáo theo dõi mà user đã xem qua, hãy coi nó là một gói
bằng chứng bổ sung để khai thác ngôn ngữ.
Không xin cookie, session, API key, ảnh chụp màn hình hay quyền truy cập trực
tiếp vào tài khoản. Chỉ rút ra ngôn ngữ khách hàng được trích dẫn, URL, mốc thời
gian và nhãn nguồn, rồi đánh dấu gói này là bằng chứng do user cung cấp trong
mục Chỗ thiếu dữ liệu và Nguồn.

ĐỊNH DẠNG ĐẦU RA:

## Phát hiện từ diễn đàn & cộng đồng

### Chủ đề thảo luận
Với mỗi chủ đề lớn tìm thấy:
- **Chủ đề:** {mọi người đang bàn về gì}
- **Khối lượng:** {số thread/bình luận ước tính}
- **Sắc thái:** tích cực / tiêu cực / lẫn lộn
- **Thread tiêu biểu:**
  - [{tiêu đề thread}]({url}) — {ý chính rút ra}

### Bản đồ ngôn ngữ
Đúng những từ khách hàng dùng — sắp xếp để tái sử dụng cho định vị và copy:

**Để mô tả vấn đề:**
- "{cụm từ chính xác}" — dùng trong {X} thread
- "{cụm từ chính xác}" — dùng trong {X} thread

**Để mô tả giải pháp mong muốn:**
- "{cụm từ chính xác}"
- "{cụm từ chính xác}"

**Để mô tả bức xúc với đối thủ:**
- "{cụm từ chính xác}" — về {competitor}
- "{cụm từ chính xác}" — về {competitor}

**Để mô tả lý do khiến họ chuyển đổi:**
- "{cụm từ chính xác}"
- "{cụm từ chính xác}"

### Các thread "Bạn dùng gì cho X?"
| Thread | Được đề xuất nhiều nhất | Xếp thứ hai | Tiêu chí chung |
|--------|----------------|-----------|-----------------|
| {title} | {tool} ({vì sao}) | {tool} | {điều mọi người quan tâm} |

### Câu chuyện chuyển đổi
Với mỗi câu chuyện chuyển đổi tìm thấy:
- **Từ:** {competitor} → **Sang:** {competitor}
- **Vì sao chuyển:** {lý do}
- **Được gì:** {lợi ích}
- **Mất gì:** {đánh đổi}
- **Có chuyển lại lần nữa không?** {có/không và vì sao}

### Tổng hợp tín hiệu rời bỏ
Gom các lý do người dùng rời bỏ đối thủ:
| Lý do | Đối thủ bị ảnh hưởng | Tần suất | Mức nghiêm trọng |
|--------|---------------------|-----------|----------|
| {reason} | {những bên nào} | thường gặp / thỉnh thoảng | cao / trung bình |

## Chỗ thiếu dữ liệu
- [Cộng đồng không tìm thấy hoặc không hoạt động cho nhóm sản phẩm này]
- [Đối thủ không hiện diện trên diễn đàn]

Lưu vào: {project-name}/raw/forum-mining.md
```
