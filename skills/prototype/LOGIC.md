# Prototype logic

Một file HTML duy nhất, tự chứa (một **bản demo chia sẻ được** — **shareable demo**) cho phép bất kỳ ai điều khiển một state model bằng cách bấm nút. Dùng khi câu hỏi xoay quanh **business logic, chuyển trạng thái hoặc hình dạng dữ liệu**: loại thứ trông hợp lý trên giấy nhưng chỉ lộ ra là sai khi đẩy qua các trường hợp thật.

Vì chỉ là một file, không cần cài gì, bạn có thể đưa nó cho người không biết code (designer, PM, chuyên gia nghiệp vụ) để họ tự cảm nhận model. Vì vậy nó nói bằng ngôn ngữ của họ, không phải ngôn ngữ của code.

## Khi nào đúng là dạng này

- "Mình không chắc state machine này xử lý được trường hợp X rồi Y."
- "Data model này có thực sự biểu diễn được trường hợp…"
- "Mình muốn cảm nhận xem API nên trông thế nào trước khi viết."
- Bất cứ khi nào ai đó muốn **bấm nút và xem state thay đổi**.

Nếu câu hỏi là "cái này nên trông thế nào" thì nhánh này sai. Dùng [UI.md](UI.md).

## Quy trình

### 1. Nêu rõ câu hỏi

Trước khi viết code, ghi ra state model nào và câu hỏi nào đang được làm prototype. Một đoạn văn, đặt ở đầu demo (trong phần giới thiệu nhìn thấy được, không chỉ trong comment). Một prototype logic trả lời sai câu hỏi là phí hoàn toàn, nên hãy viết câu hỏi ra rõ ràng để kiểm tra lại sau, dù user đang xem ngay hay quay lại xem khi rảnh.

### 2. Tách logic thành một module mang đi được

Đặt phần logic thật (phần đang trả lời câu hỏi) trong một khối `<script>` duy nhất, viết như một module nhỏ, thuần (pure), có thể nhấc ra thả vào codebase thật sau này. Trang bao quanh là đồ dùng xong bỏ; module này thì không.

Hình dạng phù hợp tuỳ vào câu hỏi:

- **Một reducer thuần**: `(state, action) => state`. Hợp khi các action là sự kiện rời rạc và state là một giá trị duy nhất.
- **Một state machine**: state và chuyển trạng thái tường minh. Hợp khi "lúc này action nào mới hợp lệ" là một phần của câu hỏi.
- **Một nhóm nhỏ hàm thuần** trên một kiểu dữ liệu đơn giản. Hợp khi không có state hiện tại ngầm định, chỉ có các phép biến đổi.
- **Một class hoặc module có bề mặt method rõ ràng** khi logic thực sự sở hữu state nội bộ kéo dài.

Chọn hình dạng khớp nhất với câu hỏi, *không phải* hình dạng dễ nối vào trang nhất. Giữ nó thuần: không DOM, không `document`, không handler của nút thò vào bên trong. Trang gọi vào module; không có chiều ngược lại. Đây là điều làm prototype còn hữu ích sau khi hết vai trò: khi câu hỏi đã được trả lời, reducer / machine / nhóm hàm đã kiểm chứng tự nhấc sang module thật được.

### 3. Dựng file HTML chia sẻ được

Một file, HTML/CSS/JS thuần: không framework, không bundler, không server, mọi thứ inline để mở bằng bấm đúp và vẫn chạy khi bị gửi qua email. Ai cũng chạy được bằng cách mở file.

Viết cho người không biết code. Mọi nhãn dùng **ngôn ngữ nghiệp vụ** (**domain language**), không dùng ngôn ngữ code: nút và state đọc như nghiệp vụ, không như reducer. Giải thích bằng lời thường chuyện gì đang xảy ra.

Bố cục phân cấp rõ ràng, từ trên xuống:

1. **Tiêu đề và một dòng giải thích** demo này cho phép khám phá điều gì (câu hỏi ở bước 1).
2. **State hiện tại**: toàn bộ state liên quan, hiển thị thành một panel dễ đọc (các trường có nhãn, không đổ JSON thô), vẽ lại sau mỗi lần bấm để thấy rõ thay đổi. Chỗ nào giúp người không biết code theo dõi được thì chỉ ra cái gì vừa thay đổi.
3. **Nút bấm tự do**: mỗi action một nút, luôn bấm được, để ai cũng chọc thử model theo bất kỳ thứ tự nào. Mỗi lần bấm dispatch action đó và vẽ lại state.
4. **Kịch bản dẫn dắt** (**guided walkthroughs**): một bộ **kịch bản** (**scenario**), mỗi kịch bản một tab. Mỗi tab có một đoạn mô tả ngắn bằng lời thường (tình huống được dựng lên và cần để ý điều gì), bên dưới là các **nút cần bấm** theo thứ tự cho kịch bản đó. Mỗi bước là một nút thật: bấm vào sẽ thực hiện action đó và chuyển sang bước tiếp. Bắt đầu một kịch bản sẽ reset về một state ban đầu xác định, để kịch bản chạy giống nhau mọi lần.

Chọn kịch bản thể hiện các trường hợp khó, những thứ khó suy luận trên giấy: luồng suôn sẻ (happy path), một edge case hóc búa, một lần thử làm điều lẽ ra không được phép.

Giữ cho đẹp nhưng tiết chế: chữ sạch, khoảng cách rộng rãi, một màu nhấn. Không animation, không trò mè: không gì được tranh chỗ với state và các nút.

### 4. Bàn giao

Gửi file cho họ, hoặc mở sẵn cho họ. Họ sẽ bấm qua các kịch bản và chơi tự do khi rảnh; khoảnh khắc đáng giá là khi họ nói "khoan, chuyện đó lẽ ra không thể xảy ra" hay "ơ, mình tưởng X sẽ khác"; đó là bug trong _ý tưởng_, và đó chính là mục đích. Nếu họ muốn thêm action hay kịch bản mới thì thêm vào. Prototype sẽ tiến hoá.

### 5. Lưu câu trả lời và prototype

Khi prototype đã trả lời xong câu hỏi, lưu câu trả lời, rồi lưu prototype theo cách [SKILL](SKILL.md) mô tả. Riêng với logic: reducer / machine / nhóm hàm đã kiểm chứng nhấc sang module thật (quyết định đã được hấp thụ); phần vỏ HTML đi theo sang nhánh dùng xong bỏ, nơi giữ prototype làm nguồn gốc, và vì là một file tự chứa nên ở đó vẫn chạy lại dễ dàng.

## Anti-pattern

- **Đừng thêm test.** Prototype mà cần test thì không còn là prototype.
- **Đừng nối vào database thật.** Dùng state trong bộ nhớ, trừ khi câu hỏi nói riêng về lưu trữ.
- **Đừng tổng quát hoá.** Không "lỡ sau này cần hỗ trợ X thì sao". Prototype trả lời một câu hỏi.
- **Đừng trộn logic và trang vào nhau.** Nếu module thuần tham chiếu tới DOM, `document` hay handler của nút thì không nhấc ra được nữa. Giữ trang là lớp vỏ mỏng bọc một module thuần.
- **Đừng dùng framework, bundler hay server.** Một file người nhận bấm đúp là chạy; một app React hay dev server phá mất tính "chia sẻ được".
- **Đừng đưa vỏ HTML lên production.** Trang được tối ưu để người bấm tay. Phần module logic phía sau mới là thứ đáng giữ.
