---
name: wayfinder
description: >-
  Lập kế hoạch cho một khối việc rất lớn (vượt sức chứa của một phiên agent)
  dưới dạng một bản đồ chung gồm các ticket quyết định trên issue tracker, rồi
  giải từng ticket một cho tới khi đường tới đích hiện rõ. Dùng khi user có một
  ý tưởng còn mơ hồ, quá lớn cho một phiên, cần tìm đường trước khi làm, hoặc
  muốn tiếp tục đi tiếp một bản đồ wayfinder đang có. Câu kích hoạt: "lập bản
  đồ cho việc này", "wayfinder", "chia việc lớn thành các quyết định", "làm
  tiếp ticket tiếp theo trên map", "chart a map for this", "work through the
  wayfinder map".
disable-model-invocation: true
---

Một ý tưởng còn lỏng lẻo vừa tới, quá lớn cho một phiên agent, và bị sương mù bao phủ: con đường từ đây tới **đích đến** (**destination**) chưa nhìn thấy được. Tìm đường (**wayfinding**) là đi tìm con đường đó, chứ không phải lao thẳng vào đích. Skill này vẽ con đường thành một **bản đồ chung** (**shared map**) trên issue tracker của repo, rồi lần lượt giải từng **ticket quyết định** (**decision ticket**: những câu hỏi mà lời giải là một quyết định, không phải một lát cắt việc xây dựng cần thực thi) cho tới khi lộ trình rõ ràng.

Đích đến khác nhau tùy mỗi nỗ lực, và gọi tên nó là bước đầu tiên của việc vẽ bản đồ: nó định hình mọi ticket. Đích có thể là một spec để bàn giao rồi tiếp tục lặp, một quyết định cần chốt trước khi bắt đầu lập kế hoạch, hoặc một thay đổi thực hiện tại chỗ như migration một cấu trúc dữ liệu. Bản đồ không gắn với domain nào: việc engineering, nội dung khoá học, gì vừa hình dạng này đều được.

## Lên kế hoạch, đừng bắt tay làm

Mặc định wayfinder là **lập kế hoạch**: mỗi ticket giải một quyết định, và bản đồ xong khi con đường đã rõ, không còn gì phải quyết trước khi ai đó bắt tay làm. Cảm giác muốn lao vào làm luôn thường là tín hiệu bạn đã tới mép bản đồ và đến lúc bàn giao. Một nỗ lực có thể ghi đè quy tắc này trong phần **Ghi chú** của nó, đưa việc thực thi vào ngay trong bản đồ; nhưng nếu không có ghi đè đó, hãy tạo ra quyết định, không phải sản phẩm.

## Gọi bằng tên

Mọi map và ticket đều là issue, nên đều có **tên**: chính là tiêu đề của nó. Trong mọi thứ con người đọc (lời tường thuật, mục Các quyết định đã chốt của map), hãy gọi nó bằng tên, không bao giờ bằng id, số hay slug trơn. Một bức tường `#42, #43, #44` thì không đọc nổi; tên thì liếc là hiểu. Id và URL không biến mất; tên bọc lấy link, nhưng chúng đi _bên trong_ cái tên, không bao giờ thay thế cái tên.

## Bản đồ

Bản đồ (**map**) là một issue duy nhất trên issue tracker của repo, gắn label `wayfinder:map`, và là sản phẩm chuẩn (**canonical artifact**). Các ticket của nó là issue con của map.

Bản đồ là một **mục lục** (**index**), không phải kho chứa. Nó liệt kê các quyết định đã đưa ra và trỏ tới những ticket giữ chi tiết; một quyết định chỉ nằm ở đúng một chỗ, là ticket của nó, nên bản đồ không bao giờ chép lại, chỉ tóm ý chính và gắn link.

**Map, ticket con, quan hệ chặn và truy vấn frontier nằm vật lý ở đâu là tùy tracker.** Lẽ ra bạn đã được cung cấp thông tin về issue tracker. Nếu chưa, bảo user chạy `/setup-agent`. Xem mục "Thao tác wayfinding" trong tài liệu tracker để biết repo _này_ biểu diễn chúng ra sao. Nếu không có tracker nào được cung cấp, mặc định dùng tracker markdown cục bộ.

### Phần thân của bản đồ

Toàn bộ bản đồ ở độ phân giải thấp, được nạp một lần mỗi phiên. Các ticket đang mở **không** được liệt kê: chúng là các issue con đang mở, tìm bằng truy vấn.

```markdown
## Đích đến

<đi tới cuối bản đồ này trông như thế nào: spec, quyết định hoặc thay đổi mà nỗ lực này đang tìm đường tới. Một hai dòng; mọi phiên đều định hướng theo nó trước khi chọn ticket.>

## Ghi chú

<domain; các skill mọi phiên nên tham khảo; những ưu tiên cố định cho nỗ lực này>

## Các quyết định đã chốt

<!-- mục lục: mỗi ticket đã đóng một dòng, đủ để đánh giá có liên quan không, rồi mở link để xem chi tiết mà ticket giữ -->

- [<tiêu đề ticket đã đóng>](link): <ý chính một dòng của câu trả lời>

## Chưa xác định rõ

<!-- xem "Sương mù chiến tranh": phần sương mù trong phạm vi mà chưa thể tạo ticket; sẽ dần chuyển thành ticket khi frontier tiến lên -->

## Ngoài phạm vi

<!-- xem "Ngoài phạm vi": việc đã được xác định là nằm sau đích đến; đóng hẳn, không bao giờ chuyển thành ticket -->
```

### Ticket

Mỗi ticket là một **issue con** của map; id issue trên tracker là danh tính của nó. Phần thân là câu hỏi, có kích cỡ vừa một phiên agent 100K token:

```markdown
## Câu hỏi

<quyết định hoặc cuộc điều tra mà ticket này giải quyết>
```

Mỗi ticket mang một label `wayfinder:<type>`, là một trong `research`, `prototype`, `grilling`, `task` (xem [Các loại ticket](#các-loại-ticket)). Label `wayfinder:` là label duy nhất mà map và ticket của nó mang, không bao giờ mang label triage như `ready-for-agent`: chúng là quyết định, không phải việc triển khai.

Một phiên **nhận** (**claim**) ticket bằng cách assign nó cho dev đang dẫn dắt bản đồ, làm việc này **đầu tiên**, trước mọi việc khác, để các phiên chạy song song bỏ qua nó. Người được assign _chính là_ sự nhận việc: một ticket đang mở mà chưa assign là chưa ai nhận.

Quan hệ chặn (**blocking**) dùng quan hệ phụ thuộc **gốc** (**native**) của tracker: điều này rất quan trọng vì nó hiển thị frontier _trực quan_ ngay trên UI của tracker, để con người thấy việc nào có thể nhận mà không cần mở bản đồ. Chỉ tracker nào không có tính năng chặn gốc mới dùng phương án dự phòng là quy ước ghi trong phần thân. Một ticket được **gỡ chặn** (**unblocked**) khi mọi ticket chặn nó đều đã đóng; **frontier** là các ticket con đang mở, không bị chặn, chưa ai nhận: mép của vùng đã biết.

Câu trả lời không nằm trong phần thân; nó được ghi lại khi giải quyết (xem [Đi qua bản đồ](#đi-qua-bản-đồ)). Tài sản (**asset**) tạo ra trong lúc giải một ticket được gắn link từ issue, không dán thẳng vào.

## Các loại ticket

Mỗi ticket hoặc là **HITL** (**human in the loop**: làm _cùng_ một người, người đó tự nói phần của mình) hoặc là **AFK**, do agent tự chạy một mình. Ticket HITL chỉ được giải qua cuộc trao đổi trực tiếp đó; agent không bao giờ đóng vai thay phần của con người (một agent grilling tự trả lời câu hỏi của chính mình là đã phá vỡ quy tắc này).

- **Research** (AFK): đọc tài liệu, API bên thứ ba, hoặc tài nguyên cục bộ như knowledge base để tìm ra một sự thật mà một quyết định đang chờ. Giải bằng một subagent: subagent tra cứu từ nguồn gốc có độ tin cậy cao (tài liệu chính thức, mã nguồn, spec), rồi ghi kết quả thành một file markdown. Dùng khi cần kiến thức nằm ngoài thư mục làm việc hiện tại.
- **Prototype** (HITL): nâng độ chi tiết của cuộc thảo luận bằng cách làm một sản phẩm cụ thể, rẻ, thô để mọi người phản hồi (một dàn ý, một bản phác, một stub, hoặc code UI/logic) — một prototype dùng xong là bỏ, chỉ đủ để trả lời câu hỏi thiết kế đang bàn. Gắn link prototype làm asset. Dùng khi câu hỏi then chốt là "nó nên trông thế nào" hoặc "nó nên hoạt động thế nào".
- **Grilling** (HITL): hội thoại. Đây là trường hợp mặc định. Luôn gọi skill `grill-with-docs` (vừa tra hỏi, vừa cập nhật GLOSSARY/ADR).
- **Task** (HITL hoặc AFK): việc thủ công phải xong trước khi có thể đưa ra một _quyết định_: không có gì để quyết, làm prototype hay nghiên cứu, nhưng cuộc thảo luận bị kẹt cho tới khi làm xong. Đăng ký một dịch vụ để đánh giá API của nó, cấp quyền truy cập, chuyển dữ liệu để thấy được hình dạng của nó. Đây là loại duy nhất _làm_ thay vì quyết, và nó có chỗ đứng vì gỡ chặn cho một quyết định, không phải vì mang về đích đến. Agent tự làm một mình khi có thể (AFK); nếu không thì đưa cho con người một checklist chính xác (HITL). Được giải khi việc đã xong; câu trả lời ghi lại những gì đã làm và mọi sự thật phát sinh (vị trí credentials, URL mới, số dòng dữ liệu) mà các ticket sau phụ thuộc vào.

## Sương mù chiến tranh

Bản đồ _cố ý_ chưa hoàn chỉnh: đừng vẽ những gì bạn chưa nhìn thấy. Bên ngoài các ticket đang sống là **sương mù chiến tranh** (**fog of war**): cái nhìn lờ mờ về những quyết định và cuộc điều tra bạn biết là sắp tới nhưng chưa thể chốt được, vì chúng treo vào những câu hỏi còn đang mở. Giải một ticket sẽ xua tan phần sương mù phía trước nó, chuyển (**graduate**) những gì giờ đã xác định được thành ticket mới, từng cái một, cho tới khi đường tới đích rõ ràng và không còn ticket nào.

Mục **Chưa xác định rõ** của bản đồ là nơi ghi lại cái nhìn lờ mờ đó: câu hỏi phỏng đoán, khu vực cần quay lại sau. Đó là frontier chưa được khám phá _hướng về_ đích đến: mọi thứ ở đây đều trong phạm vi, chỉ là chưa đủ sắc nét để tạo ticket. Viết sơ sài hay đầy đủ tùy tầm nhìn cho phép; nó cũng là biển chỉ đường cho cộng sự đọc để biết nỗ lực đang hướng về đâu.

**Sương mù hay ticket?** Phép thử là bạn có thể phát biểu câu hỏi một cách chính xác ngay bây giờ hay không, _chứ không phải_ bạn có trả lời được nó ngay bây giờ không.

- **Tạo ticket khi** câu hỏi đã sắc nét, kể cả khi nó đang bị chặn và bạn chưa thể làm gì với nó.
- **Ghi vào Chưa xác định rõ khi** bạn chưa thể diễn đạt nó sắc nét như vậy. Đừng cắt sẵn sương mù thành từng mẩu cỡ ticket: nó thô hơn một ticket, và một mảng sương mù có thể chuyển thành nhiều ticket, hoặc chẳng ticket nào, khi frontier tới được nó.

**Chưa xác định rõ** không bao gồm những gì đã quyết (Các quyết định đã chốt), những gì đã là ticket đang sống, và những gì ngoài phạm vi (mục tiếp theo).

## Ngoài phạm vi

Sương mù chỉ tụ lại _hướng về_ đích đến. Đích đến cố định phạm vi, nên việc nằm sau nó là **ngoài phạm vi** (**out of scope**): nó không phải sương mù, và không thuộc về **Chưa xác định rõ**. Nó có mục riêng **Ngoài phạm vi** trên bản đồ: những việc bạn đã chủ động loại khỏi nỗ lực _này_. Thứ đưa nó vào đây là phạm vi, không phải độ sắc nét.

Việc ngoài phạm vi không bao giờ chuyển thành ticket (frontier dừng ở đích đến), nên nó chỉ quay lại nếu đích đến được vẽ lại, và khi đó là một nỗ lực mới, không phải tiếp tục cái cũ.

Loại một thứ ra ngoài phạm vi là một hành động xác định phạm vi, không phải một bước trên lộ trình. Khi một ticket đã tồn tại hoá ra nằm sau đích đến (bị đưa nhầm vào phạm vi lúc vẽ bản đồ, hoặc lộ ra sau một lời giải), hãy **đóng nó** (ticket đã đóng thì rõ ràng là nằm ngoài frontier) và để lại một dòng trong mục **Ngoài phạm vi**: ý chính kèm lý do nó nằm ngoài phạm vi, gắn link tới ticket đã đóng. Nó không nằm trong **Các quyết định đã chốt**, mục ghi lại lộ trình thực sự đã đi; một ranh giới phạm vi không phải là một bước trên lộ trình đó.

## Cách gọi skill

Có hai chế độ. Ở chế độ nào cũng vậy, **không bao giờ giải quá một ticket mỗi phiên**, ngoại trừ ticket research.

### Vẽ bản đồ

User gọi skill kèm một ý tưởng còn lỏng lẻo.

1. **Gọi tên đích đến.** Gọi skill `grill-with-docs` để chốt bản đồ này đang tìm đường tới đâu: spec, quyết định hay thay đổi. Đích đến cố định phạm vi, nên nó được chốt trước tiên.
2. **Vẽ frontier.** Tra hỏi (grill) tiếp, lần này theo **chiều rộng** (**breadth-first**): toả ra khắp toàn bộ không gian thay vì đào sâu vào một mạch nào, làm lộ ra các quyết định còn mở và những bước đầu tiên có thể làm ngay. **Nếu bước này không làm lộ ra chút sương mù nào** (đường tới đích đã rõ, cả hành trình đủ nhỏ cho một phiên), bạn không cần bản đồ. Dừng lại và hỏi user muốn tiếp tục thế nào.
3. **Tạo bản đồ** (label `wayfinder:map`): điền Đích đến và Ghi chú, để trống Các quyết định đã chốt, phác phần sương mù vào **Chưa xác định rõ**.
4. **Tạo các ticket bạn có thể xác định ngay** dưới dạng issue con của map, rồi nối các cạnh chặn trong **lượt thứ hai** (issue cần có id trước khi có thể tham chiếu lẫn nhau). Viết các tham chiếu chéo cũng trong lượt đó, bằng id thật: một placeholder `#<n>` sẽ tự động link tới một issue không liên quan. Việc nối cạnh sắp xếp chúng thành frontier và nhóm bị chặn; mọi thứ bạn chưa xác định được thì ở lại trong sương mù: mục **Chưa xác định rõ**.
5. **Phóng các subagent research.** Với mỗi ticket `research` vừa tạo, khởi một subagent với context window mới để giải nó song song: subagent tra cứu từ nguồn gốc có độ tin cậy cao, ghi kết quả thành file markdown trên một nhánh tạm dùng xong bỏ `research/<name>`, kèm một con trỏ ngữ cảnh từ ticket tới đó. Push nhánh nhưng không mở PR: nhánh này không bao giờ được merge.
6. Dừng: vẽ bản đồ là việc của một phiên; nó không tự tay giải ticket nào.

### Đi qua bản đồ

User gọi skill kèm một bản đồ (URL hoặc số). Ticket là **tuỳ chọn**: nếu không có, chính bạn chọn quyết định tiếp theo, không phải user.

1. Nạp **bản đồ**: cái nhìn độ phân giải thấp, không phải mọi phần thân ticket.
2. Chọn ticket. Nếu user đã nêu tên một ticket, dùng nó. Nếu không, lấy ticket đầu tiên của frontier theo thứ tự. **Nhận nó**: assign cho chính mình trước mọi việc khác.
3. Giải nó theo đúng loại mà label `wayfinder:<type>` chỉ ra (xem [Các loại ticket](#các-loại-ticket)). Đọc label, không chỉ đọc phần thân: phần thân không bao giờ ghi loại. **Phóng to khi cần**: lấy toàn bộ phần thân của bất kỳ ticket liên quan hay đã đóng nào khi cần; gọi các skill mà mục `## Ghi chú` nêu tên. Nếu phân vân, gọi skill `grill-with-docs`.
4. Ghi lại lời giải: đăng câu trả lời dưới dạng **bình luận giải quyết** (**resolution comment**), **đóng** issue, và **nối một con trỏ ngữ cảnh** vào mục Các quyết định đã chốt của bản đồ.
5. Thêm các ticket mới lộ ra (tạo trước, nối cạnh sau); chuyển mọi phần sương mù mà câu trả lời đã làm cho xác định được thành ticket, xoá từng mảng đã chuyển khỏi **Chưa xác định rõ** để nó chỉ còn tồn tại dưới dạng ticket mới. Nếu câu trả lời cho thấy một ticket (ticket này hoặc ticket khác) nằm sau đích đến, **loại nó ra ngoài phạm vi** thay vì giải nó trên lộ trình. Nếu quyết định làm mất hiệu lực những phần khác của bản đồ, cập nhật hoặc xoá các ticket đó.

User có thể chạy song song các ticket không bị chặn, nên hãy dự trù rằng các phiên khác đang sửa tracker cùng lúc.
