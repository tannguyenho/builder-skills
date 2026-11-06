# Quy tắc dịch skill từ repo gốc

Dùng khi dịch phần thay đổi của một skill đã có, hoặc dịch một skill gốc mới. Bộ skill này giữ một giọng văn và một bộ thuật ngữ thống nhất, nên mỗi đoạn dịch thêm phải đọc như được viết cùng lúc với phần còn lại. Trước khi dịch, mở bản tiếng Việt hiện có của skill để bắt đúng giọng.

## Đổi tên skill

| Gốc | Trong bộ này |
| --- | --- |
| `setup-matt-pocock-skills` (và lệnh `/setup-matt-pocock-skills`) | `setup-agent` (`/setup-agent`) |
| `startup-design` | `product-design` |
| `startup-competitors` | `product-competitors` |
| các skill khác đã dịch | giữ nguyên tên |

Tên đầy đủ của từng skill và nguồn của nó nằm trong `upstream.json`.

## Skill gốc không có trong bộ này

Khi bản gốc gọi tới một skill mà bộ này không có:

- `grilling` → skill `grill-me` (chứa toàn bộ nội dung grilling).
- `grilling` + `domain-modeling` cùng lúc, hoặc chỉ `domain-modeling` → skill `grill-with-docs`.
- `tdd` → file `references/tdd.md` của chính skill (chỉ `implement` và `implement-spec` có file này).
- Các skill khác (`handoff`, `show-me`, `teach`, `startup-pitch`, `startup-positioning`…): viết lại thành một chỉ dẫn ngắn tự đủ ngay tại chỗ, hoặc bỏ phần nhắc tên. Không để lời gọi tới skill không tồn tại; script `audit.py check` sẽ báo lỗi.

Nếu một skill gốc mới trở thành phụ thuộc quan trọng của nhiều skill, đề xuất user dịch luôn skill đó thay vì viết chỉ dẫn tạm. Đó chính là cách `research` và `prototype` được thêm vào bộ này.

## Dịch

1. **Dịch đủ, không tóm tắt, không thêm ý.** Ngoại lệ duy nhất là các `adaptations` ghi trong `upstream.json`.
2. Giữ cấu trúc heading, danh sách, bảng, code block.
3. **Giữ tiếng Anh:**
   - tên file, đường dẫn, lệnh, code, placeholder;
   - label trên tracker (`needs-triage`, `ready-for-agent`, `wayfinder:*`…);
   - trường dạng khoá (`Status:`, `Type:`, `Blocked by:`);
   - nhãn mà bước kiểm chứng dò theo (`[Data]`, `[Estimate]`, `[Assumption]`, GO/NO-GO);
   - từ khoá tìm kiếm;
   - thuật ngữ chuẩn (TAM/SAM/SOM, JTBD, ADR, PR, seam, deep module, module/interface/adapter…).

   Lần đầu một thuật ngữ quan trọng xuất hiện, viết dạng "tiếng Việt (**term gốc**)".
4. **Dịch sang tiếng Việt:** lời giảng; template mà agent sẽ ghi ra (heading của spec, ticket, báo cáo); chuỗi hiển thị cho người dùng trong script.
5. **Script** (`.sh`, `.py`): code giữ nguyên, chỉ dịch comment và chuỗi hiển thị. Không đổi chuỗi mà code so khớp (vd `[y/N]` khi regex kiểm `^[Yy]`).
6. **Frontmatter:**
   - `name` trùng tên thư mục;
   - `description` viết tiếng Việt dạng `>-`, nói rõ làm gì và khi nào dùng, kèm vài câu kích hoạt tiếng Việt và tiếng Anh;
   - giữ `disable-model-invocation: true` nếu gốc có, **trừ khi** skill đó bị skill khác gọi.
7. **Không đưa vào skill:** `agents/openai.yaml`, `CREDITS.md`, `metadata.credits`.
8. **Repo public:** không token, không email, không link Figma/Drive nội bộ.
9. Ngôn ngữ đầu ra mặc định của các skill nghiên cứu (`product-*`) là tiếng Việt.

## Sau khi dịch

- Đổi heading thì phải sửa luôn link anchor trỏ tới heading đó (vd `#các-loại-ticket`).
- Sửa `references/tdd.md` thì sửa giống hệt ở cả `implement` và `implement-spec`.
- Chạy `python skills/doctor-audit/scripts/audit.py check <skill>`.
