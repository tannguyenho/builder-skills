---
name: writing-for-agents
description: >-
  Cách viết tài liệu cho agent đọc: skill, AGENTS.md / CLAUDE.md, tài liệu được
  trỏ tới. Dùng khi tạo hoặc sửa skill, hoặc sửa AGENTS.md hay CLAUDE.md. Câu
  kích hoạt: "viết skill mới", "sửa CLAUDE.md", "rút gọn mô tả skill này",
  "write a skill", "edit AGENTS.md".
---

Tài liệu tham khảo để viết mọi văn bản mà agent tiêu thụ: một skill, một `AGENTS.md` / `CLAUDE.md`, một tài liệu được tới qua một con trỏ. Cách đóng gói khác nhau; cách viết thì không: cùng những đòn bẩy đó làm mỗi văn bản trở nên dễ đoán, vì agent đi theo cùng một _quy trình_ mỗi lần chạy chứ không phải tạo ra cùng một output.

Khi văn bản bạn đang viết là một skill, đọc [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) về frontmatter, lựa chọn cách gọi (invocation) và router skill.

## Con trỏ ngữ cảnh

**Con trỏ ngữ cảnh** (**context pointer**) là một tham chiếu nằm trong context của agent, gọi tên một tài liệu nằm ngoài context và mã hoá điều kiện để tìm tới nó. Description của một skill là một con trỏ; một dòng trong `AGENTS.md` nêu tên một tài liệu cũng là cùng một thứ. _Cách diễn đạt_ của con trỏ, chứ không phải đích của nó, quyết định khi nào agent tìm tới tài liệu, và chắc chắn đến đâu. Một đích bắt buộc phải có nằm sau một con trỏ diễn đạt yếu là một bug về độ dao động (variance): hãy mài sắc cách diễn đạt trước, và chỉ đưa thẳng tài liệu vào (inline) nếu mài sắc không ăn thua.

Một con trỏ làm hai việc: nói tài liệu là gì, và liệt kê các **nhánh** (**branches**) cần kích hoạt việc tìm tới nó (một nhánh là một trường hợp riêng biệt mà văn bản xử lý, nên các lần chạy khác nhau đi theo các đường khác nhau qua nó). Mỗi chữ của một con trỏ luôn-được-nạp đều tốn chi phí ở mọi lượt, nên nó cần được tỉa còn gắt hơn cả phần thân:

- **Đưa leading word lên đầu**: con trỏ là nơi nó làm việc kích hoạt.
- **Mỗi nhánh một câu kích hoạt.** Các từ đồng nghĩa chỉ đổi tên cho một nhánh là một nhánh viết hai lần; gộp chúng lại và chỉ giữ những nhánh thật sự khác nhau.
- **Cắt phần giới thiệu danh tính mà phần thân đã mang.**

## Hai loại tải

Mỗi văn bản và con trỏ bạn thêm vào đều tiêu một trong hai ngân sách:

- **Tải ngữ cảnh** (**context load**) là chi phí của tài liệu luôn-được-nạp lên context window của agent: một dòng `AGENTS.md`, một description của skill, bất cứ thứ gì nằm trong context ở mọi lượt, tiêu token và sự chú ý dù nó có được kích hoạt hay không.
- **Tải nhận thức** (**cognitive load**) là chi phí đặt lên con người: có những văn bản nào và khi nào dùng cái nào. Con người chính là bảng mục lục. Đây không phải chi phí cần giảm tối đa: nó là cái giá của quyền chủ động của con người; hãy tiêu nó ở chỗ cần phán đoán của con người, bỏ nó đi ở chỗ không cần.

Tài liệu chỉ được tới qua một con trỏ thoát khỏi tải ngữ cảnh với cái giá là dòng của chính con trỏ; tài liệu không có con trỏ nào thì nằm hoàn toàn trên tải nhận thức.

## Thang thông tin

Một văn bản được dựng từ hai loại nội dung: **bước** (**steps**: các hành động có thứ tự mà agent thực hiện) và **tham khảo** (**reference**: định nghĩa, quy tắc, sự kiện được tra khi cần). Hai loại trộn lẫn tự do: toàn bước (một công thức), toàn tham khảo (bộ quy tắc của một lần review, chính skill này), hoặc cả hai. Quyết định cốt lõi là mỗi phần nằm ở đâu trên **thang thông tin** (**information hierarchy**), một chiếc thang xếp hạng theo mức agent cần tài liệu đó ngay đến đâu:

1. **Bước trong file** là tầng chính: agent làm gì, theo thứ tự nào.
2. **Tham khảo trong file** được tra khi cần. Thường là một tập ngang hàng phẳng một cách chính đáng (mọi quy tắc của một lần review trên cùng một bậc), đó là cách sắp xếp ổn, không phải dấu hiệu xấu.
3. **Tham khảo được tách ra** (**disclosed reference**) được đẩy ra một file riêng, tới được qua một con trỏ ngữ cảnh, chỉ nạp khi con trỏ được kích hoạt. Trải từ một file anh em trong cùng thư mục đến tham khảo hoàn toàn bên ngoài, nằm ở đâu cũng được và văn bản nào cũng trỏ tới được.

Đẩy xuống quá ít thì phần trên phình to; đẩy quá nhiều thì bạn giấu mất thứ agent thực sự cần. Thế giằng co đó chính là toàn bộ quyết định.

**Tiết lộ dần** (**progressive disclosure**) là động tác đi xuống thang (ra khỏi file chính và ra sau một con trỏ) để phần trên luôn dễ đọc. Chủ yếu không phải để tối ưu token: đó là cách bảo vệ thứ bậc. Phân nhánh là phép thử tách gọn nhất: inline những gì mọi nhánh đều cần, và đẩy ra sau con trỏ những gì chỉ một số nhánh mới tới. Khi văn bản có các bước, phần tham khảo trong file lẽ ra nên tách ra sẽ chôn vùi các bước và biến việc chú ý tới chúng thành trò tung đồng xu: một đòn bẩy về độ dao động, không chỉ về độ dễ đọc.

**Đặt cạnh nhau** (**co-location**) là người bạn đồng hành bên trong file: nếu chiếc thang quyết định một phần nằm _thấp đến đâu_, thì co-location quyết định _cái gì nằm bên cạnh nó_ khi đã ở đó. Giữ định nghĩa, quy tắc và lưu ý của một khái niệm dưới cùng một heading thay vì rải rác, để đọc một phần là kéo theo các phần lân cận. Phép thử: văn bản phải đọc như tài liệu được viết cho agent. Nội dung được gom nhóm thì đọc như vậy; nội dung rải rác thì không. (Khác với trùng lặp: trùng lặp lặp lại một ý ở hai chỗ; rải rác thì xé một ý ra nhiều mảnh.)

**Dàn trải** (**sprawl**) là kiểu thất bại ở đây: một văn bản đơn giản là quá dài, kể cả khi mọi dòng đều còn sống và không trùng. Sự chú ý mỏng dần trên phần dư, và mỗi dòng thêm là một dòng nữa phải giữ cho còn liên quan. Cách chữa là chiếc thang: tách phần tham khảo ra sau con trỏ, và chia theo nhánh hoặc theo trình tự để mỗi đường đi chỉ mang những gì nó cần.

## Bước và tiêu chí hoàn thành

Mỗi bước kết thúc bằng một **tiêu chí hoàn thành** (**completion criterion**), điều kiện cho agent biết việc đã xong. Hai thuộc tính biến nó thành một đòn bẩy:

- **Độ rõ**: agent có phân biệt được xong và chưa xong không? Một giới hạn mơ hồ ("đã hiểu ra") mời gọi **hoàn thành sớm** (**premature completion**): kết thúc bước trước khi nó thật sự xong, sự chú ý trượt sang việc _được xong_. Các bước còn hiện ra phía trước (**các bước sau-hoàn-thành**, **post-completion steps**) tạo lực kéo; độ rõ của tiêu chí là lực cản. Phòng thủ theo thứ tự: **mài sắc giới hạn trước** (cục bộ và rẻ); chỉ khi nó mơ hồ không thể khắc phục _và_ bạn quan sát thấy agent vội vàng, mới giấu các bước sau bằng cách chia nhỏ trình tự. Việc giấu chỉ có tác dụng qua một ranh giới context thật (một lần bàn giao hoặc một lần phái subagent; một lời gọi inline vẫn để các bước sau trong context và chẳng xoá được gì).
- **Mức đòi hỏi** (**demand**): nó đòi hỏi bao nhiêu. "Mọi model đã sửa đều được tính đến" buộc làm kỹ ở chỗ "tạo một danh sách thay đổi" thì không. Mức đòi hỏi thúc đẩy **phần việc đào bới** (**legwork**: việc đào sâu mà agent làm bên trong công việc, ẩn trong cách diễn đạt chứ không được viết thành một bước riêng), và nó không bị gắn với bước: "mọi quy tắc đều được áp dụng" ràng buộc một khối tham khảo phẳng y như "mọi bước đều xong" ràng buộc một trình tự, đó là cách một văn bản toàn tham khảo vẫn mang một chuẩn về độ đầy đủ.

Tiêu chí mạnh nhất là vừa kiểm tra được vừa đầy đủ.

## Khi nào nên tách

Tách một văn bản thành hai là tiêu một trong hai loại tải, nên chỉ tách khi đường cắt xứng đáng:

- **Theo trình tự**: tách một chuỗi bước khi các bước sau-hoàn-thành cám dỗ agent làm vội bước trước mặt. Giữ chúng khuất tầm nhìn sẽ thúc đẩy nhiều legwork hơn cho việc hiện tại. Coi chừng chiều ngược lại: gộp các trình tự sẽ phơi các bước sau của mỗi bước ra cho phần tiếp theo, mời gọi hoàn thành sớm.
- **Theo cách gọi**, riêng cho skill: xem [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md).

## Leading word

**Leading word** (từ dẫn dắt) là một khái niệm gọn đã sẵn có trong dữ liệu pretraining của model, mà agent dùng để suy nghĩ khi chạy văn bản (_lesson_, _fog of war_, _tracer bullets_). Được lặp lại như một token, không bao giờ như một câu, nó tích luỹ một định nghĩa phân tán và neo cả một vùng hành vi bằng ít token nhất, nhờ huy động những hiểu biết sẵn có mà model đã nắm. Tự đặt từ mới cũng được nếu bạn định nghĩa rõ, nhưng một từ tự chế không huy động được hiểu biết sẵn có nào: bạn trả bằng token định nghĩa thứ mà một từ có sẵn trong pretraining cho không; hãy tìm từ có sẵn trước.

Nó neo hai lần. Trong phần thân, ở khâu _thực thi_: agent tìm tới cùng một hành vi mỗi khi từ đó xuất hiện, và bên trong phần tham khảo phẳng nó hướng sự chú ý vào một loại thứ cần tìm. Trong con trỏ, ở khâu _gọi_: khi cùng một từ sống trong prompt, tài liệu và codebase của bạn, agent nối ngôn ngữ chung đó với tài liệu và tìm tới nó chắc chắn hơn.

Hãy săn cơ hội refactor bằng leading word. Một bộ ba được viết ra đầy đủ ở ba chỗ, một con trỏ tốn cả một câu để ám chỉ một ý. Mỗi chỗ như vậy là một đoạn đang chờ được gộp lại thành một token duy nhất:

- "fast, deterministic, low-overhead" (nhanh, tất định, ít chi phí) → _tight_ (một vòng lặp _tight_).
- "a loop you believe in" (một vòng lặp bạn tin vào) → _red_, biến một cổng mơ hồ thành một trạng thái nhị phân quan sát được (vòng lặp chuyển _red_ trên bug, hoặc không).

Bạn thắng hai lần: ít token hơn, và một cái móc sắc hơn để agent treo suy nghĩ lên. Hãy mặc định rằng văn bản nào cũng đang mang những đoạn diễn đạt lại mà leading word có thể thay thế. Đi tìm chúng.

**Phủ định** (**negation**) là kiểu thất bại nằm cạnh đòn bẩy này: điều hướng bằng lệnh cấm kéo hành vi bị cấm vào context và làm nó _dễ xuất hiện hơn_, chứ không phải ít đi. _Đừng nghĩ tới con voi_, và con voi là tất cả những gì còn lại; phủ định là một bổ ngữ yếu mà khái niệm được kích hoạt mạnh đè lên, nên lệnh cấm đọc giống một nửa lời bảo hãy làm điều đó. Hãy prompt theo hướng **khẳng định**: nêu hành vi đích ("viết comment một dòng") để hành vi bị cấm không bao giờ được nhắc tới. Một lệnh cấm chỉ xứng đáng có chỗ khi là một hàng rào bảo vệ cứng mà bạn không diễn đạt khẳng định được; ngay cả khi đó, hãy ghép nó với mục tiêu khẳng định để sự chú ý đậu vào việc cần làm.

## Tỉa gọn

- Giữ mỗi ý ở một **nguồn sự thật duy nhất** (**single source of truth**): một chỗ có thẩm quyền, để thay đổi hành vi chỉ là sửa một chỗ. **Trùng lặp** (**duplication**: cùng một ý ở nhiều hơn một chỗ) tốn công bảo trì và token, và đẩy độ nổi bật của ý đó trên thang lên quá thứ hạng thật của nó. (Là mặt trái vô tình của leading word, thứ cố ý lặp lại một token, không bao giờ lặp lại ý.)
- **Môi trường** (**environment**) cũng là một nguồn sự thật (các script trong `package.json`, file cấu hình, cấu trúc thư mục, output của `--help`), và một văn bản nhắc lại nó là một **bản cache**: bản sao của một lần tra cứu, chỉ đáng gánh tải khi việc tra cứu tốn kém. Hãy cache những gì agent không tự tìm ra bằng cách nhìn: quy ước không thành văn, lý do đằng sau một lựa chọn, cái bẫy mà không file cấu hình nào thú nhận. Để những lần tra cứu chỉ cần một file, một lệnh cho môi trường lo, nơi chúng không thể lỗi thời.
- Kiểm tra từng dòng về **độ liên quan** (**relevance**): nó còn dính dáng tới việc văn bản làm không? Một dòng mất liên quan khi nó chưa bao giờ dính tới nhiệm vụ (chỉ là lời giải thích suông, hoặc một nhánh lẽ ra nên tách ra) hoặc khi nó lỗi thời vì hành vi hay thế giới nó mô tả đã thay đổi. Văn bản ngắn hơn thì dễ giữ cho còn liên quan hơn. Không có kỷ luật tỉa gọn, số phận mặc định là **trầm tích** (**sediment**): những lớp cũ lắng xuống vì thêm vào thì cảm thấy an toàn còn xoá đi thì cảm thấy rủi ro, cho đến khi bạn phải khoan xuyên qua chúng mới tìm được phần còn sống.
- Săn **lệnh vô tác dụng** (**no-op**) từng câu một: một chỉ dẫn mà model vốn đã tuân theo mặc định thì tốn tải mà chẳng nói gì. Phép thử (nó có thay đổi hành vi so với mặc định không?) tuỳ thuộc vào model, không tuỳ thuộc người đọc: hai người bất đồng về một no-op là bất đồng về hành vi mặc định, và giải quyết bằng cách chạy thử văn bản, không phải bằng tranh luận. Khi một câu không qua phép thử, xoá cả câu thay vì cắt bớt vài chữ. Phép thử này cũng chấm điểm leading word: một từ quá yếu để thắng hành vi mặc định (_be thorough_ – "hãy kỹ lưỡng" – khi agent vốn đã khá kỹ) là một no-op, và cách sửa là một từ mạnh hơn (_relentless_ – "không khoan nhượng"), chứ không phải một kỹ thuật khác.
