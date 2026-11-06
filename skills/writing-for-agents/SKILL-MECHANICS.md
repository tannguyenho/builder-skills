# Cơ chế của skill

Nhánh riêng cho skill của [`writing-for-agents`](SKILL.md): những gì thay đổi khi văn bản là một skill (frontmatter, lựa chọn cách gọi, và router skill). Mọi thứ khác về cách viết nằm ở phần tham khảo chung trong `SKILL.md`.

## Cách gọi (invocation)

Hai lựa chọn, đánh đổi giữa hai loại tải:

- Skill **model gọi được** (**model-invoked**) giữ một `description`, để agent có thể tự kích hoạt nó, và các skill khác có thể tới được nó. Bạn vẫn gõ tên nó được: model-invocation luôn _bao gồm_ cả việc user gọi tới; description chỉ thêm khả năng để agent tự phát hiện, không bao giờ bớt đi quyền của con người. Description là con trỏ ngữ cảnh cấp cao nhất của skill, buộc phải luôn được nạp: tải ngữ cảnh thường trực để đổi lấy khả năng được phát hiện. Một skill model gọi được mà toàn bộ nội dung là tham khảo cũng là một nơi chứa tham khảo dùng chung: skill khác có thể gọi nó, nên phần tham khảo mà nhiều skill cùng cần nằm ở một chỗ. Cơ chế: bỏ `disable-model-invocation`, và viết một description hướng tới model mang các nhánh kích hoạt (các quy tắc viết con trỏ trong `SKILL.md` áp dụng đầy đủ).
- Skill **user gọi** (**user-invoked**) đưa description ra khỏi tầm với của agent: chỉ con người gõ tên nó mới gọi được, và không skill nào khác gọi được. Không tốn tải ngữ cảnh, nhưng tiêu tải nhận thức: bạn là bảng mục lục phải nhớ nó tồn tại. Cơ chế: đặt `disable-model-invocation: true`; `description` trở thành thứ hướng tới con người: một dòng tóm tắt, bỏ danh sách câu kích hoạt.

Chỉ chọn model-invocation khi agent phải tự tới được skill, hoặc một skill khác phải tới được nó. Nếu nó chỉ bao giờ được gọi bằng tay, hãy để user gọi và không trả tải ngữ cảnh nào.

Phần tham khảo dùng chung mà hai skill user-gọi cùng cần thì không thể nằm trong skill nào cả: không có description, skill này không gọi được skill kia. Đẩy nó ra một file thường nằm ngoài hệ thống skill: tham khảo bên ngoài mà skill nào cũng trỏ tới được.

## Tách theo cách gọi

Đường cắt theo cách gọi của việc tách (đường cắt theo trình tự nằm trong `SKILL.md`): tách ra một skill model gọi được khi bạn có một leading word riêng biệt cần tự mình kích hoạt nó (một từ kích hoạt bạn thực sự dùng trong prompt), hoặc một skill khác phải tới được nó. Bạn trả tải ngữ cảnh cho description luôn-được-nạp mới, nên khả năng tới được độc lập đó phải xứng đáng.

## Router skill

Khi số skill user-gọi tăng lên quá mức bạn nhớ nổi, đống tải nhận thức chồng chất đó được chữa bằng một **router skill**: một skill user-gọi nêu tên các skill khác và khi nào dùng từng cái, để con người chỉ cần nhớ một skill thay vì nhiều. Nó chỉ có thể gợi ý, không bao giờ kích hoạt chúng được: skill user-gọi không có description, nên ngoài con người ra không gì tới được chúng.
