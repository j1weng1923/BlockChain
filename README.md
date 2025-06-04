# BlockChain Rút thăm trúng thưởng trong lớp học

## Giới thiệu
Dự án Blockchain nhằm xây dựng hệ thống rút thăm trúng thưởng phi tập trung trên nền tảng Ethereum.

## Tính năng chính
- Triển khai hợp đồng thông minh (Smart Contract) trên mạng Sepolia testnet.
- Giao diện người dùng để tham gia rút thăm.
- Hiển thị kết quả ngẫu nhiên, minh bạch.

## Công nghệ sử dụng
- Solidity cho hợp đồng thông minh.
- HTML cho frontend.
- Firebase cho backend.
- MetaMask để kết nối ví.

## Luồng hoạt động chính

![Hợp Đồng Thông Minh](images/Picture1.png)

- Giao diện

![Kết nối đến ví metamask](images/Picture2.png)

- Kết nối đến ví metamask

![Tải file danh sách sinh viên lên](images/Picture3.png)

- Tải file danh sách sinh viên lên

![Hiển thị danh sách sinh viên tham gia](images/Picture4.png)

- Hiển thị danh sách sinh viên tham gia

![Rút thăm tìm ra người may mắn](images/Picture5.png)

- Rút thăm tìm ra người may mắn

![Mã hash và thông tin người chiến thắng được gửi lên BlockChain](images/Picture6.png)

- Mã hash và thông tin người chiến thắng được gửi lên BlockChain

![Đồng thời lưu trên firebase để dễ dàng quản lý](images/Picture7.png)

- Đồng thời lưu trên firebase để dễ dàng quản lý

## Hướng dẫn chạy dự án

Dự Án Rút thăm trúng thưởng trong lớp học
Đây là một hệ thống rút thăm may mắn trên web, được xây dựng bằng Web3.js, Firebase và MetaMask. Hệ thống cho phép người tham gia được thêm vào thủ công hoặc qua file CSV, chọn ngẫu nhiên người thắng và tích hợp với smart contract đã được triển khai trên Ethereum.

Tính Năng:
Kết Nối MetaMask: Cho phép tương tác với blockchain Ethereum.

Thêm Người Tham Gia: Thêm thủ công hoặc tải lên file CSV.

Chọn Người Thắng Ngẫu Nhiên: Tên người tham gia được xáo trộn và người thắng được làm nổi bật.

Hiệu Ứng Pháo Hoa: Mừng chiến thắng với hiệu ứng pháo hoa.

Lưu Kết Quả: Lưu thông tin người thắng vào Firebase và smart contract trên Ethereum.

Yêu Cầu:
MetaMask: Đảm bảo bạn đã cài đặt và cấu hình MetaMask.

Firebase: Cấu hình Firebase trong dự án và thay thế thông tin cấu hình Firebase trong script.

Web3.js: Cần thiết để tương tác với Ethereum.

Confetti.js: Tạo hiệu ứng pháo hoa khi người thắng được chọn.

Hướng Dẫn Cài Đặt:
Clone Repository:

bash
Copy
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Cài Đặt Các Thư Viện Phụ Thuộc:
Dự án này không yêu cầu cài đặt thư viện ngoài vì các thư viện như Web3.js, Confetti và Firebase đã được tải từ các nguồn CDN. Đảm bảo kết nối internet ổn định để tải chúng.

Cấu Hình Firebase:

Truy cập Firebase Console.

Tạo một dự án mới và cấu hình Firebase Firestore.

Thay thế cấu hình Firebase trong script bằng thông tin của bạn.

Triển Khai Smart Contract:

Bạn cần một ví Ethereum (MetaMask) và một mạng thử nghiệm của Ethereum.

Thay thế địa chỉ smart contract trong script bằng địa chỉ smart contract của bạn.

Chạy Dự Án:
Mở tệp index.html trong trình duyệt.

Tương Tác với Ứng Dụng:

Kết Nối MetaMask với blockchain.

Thêm Người Tham Gia thủ công hoặc tải lên file CSV.

Rút Thăm Người Thắng và xem hiệu ứng hoạt hình và pháo hoa.
