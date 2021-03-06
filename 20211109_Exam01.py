{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "20211109-Exam01.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPV2luPYEpA+6tX/iEwkTlm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ndn96/my-home-work/blob/main/20211109_Exam01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i9dtcxo3PmPw"
      },
      "source": [
        "1. HƯỚNG DẪN SỬ DỤNG:\n",
        "Code này sử dụng tốt khi dùng với Pycharm tại môi trường local."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6qdy3FBYO0SN"
      },
      "source": [
        "# Bài 1: Viết chương trình thực hiện các yêu cầu sau:\n",
        "# - Nhập một chuỗi kí tự từ bàn phím\n",
        "inputString1 = input(\"Mời bạn nhập vào 1 chuỗi ký tự: \")\n",
        "# - Nhập tên tập tin từ bàn phím\n",
        "fileName1 = input(\"Mời bạn nhập vào tên tập tin: \")\n",
        "# - Lưu chuỗi ký tự ở trên vào tập tin.\n",
        "# B1: Mở 1 file cấp quyền chỉ để ghi(\"w+\"),tạo ra nó nếu nó chưa tồn tại:\n",
        "readFileName1 = open(f'{fileName1}.txt',\"w+\")\n",
        "# B2: Ghi nội dung vào file:\n",
        "readFileName1.write(inputString1)\n",
        "# B3: Đóng lại file khi hoàn thành ghi.\n",
        "readFileName1.close()\n",
        "# B4: Thông báo đã hoàn thành ghi.\n",
        "print(\"Hoàn tất ghi!\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uKJOuhSePQGi"
      },
      "source": [
        "# Bài 2: Viết chương trình thực hiện các yêu cầu sau:\n",
        "# - Nhập tên tập tin từ bàn phím\n",
        "# - Đọc nội dung tập tin và in ra màn hình\n",
        "def readFileWithName():\n",
        "    try:\n",
        "        fileName2 = input(\"Mời bạn nhập vào tên tập tin: \")\n",
        "        # Mở file:\n",
        "        file1 = open(f'{fileName2}.txt', \"r\")\n",
        "        # Reading from file:\n",
        "        print(\"*********************************\")\n",
        "        print(file1.read())\n",
        "        print(\"*********************************\")\n",
        "        file1.close()\n",
        "    except:\n",
        "        print(\"File bị lỗi hoặc tên không tồn tại!\\nVui lòng nhập đúng tên file!\")\n",
        "        readFileWithName()\n",
        "readFileWithName()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nOmI2bcRPUm4"
      },
      "source": [
        "# Bài 3: Viết chương trình thực hiện các yêu cầu sau:\n",
        "# - Nhập tên tập tin từ bàn phím\n",
        "# - Nhập một chuỗi kí tự vào từ bàn phím\n",
        "# - Ghi chuỗi kí tự này vào cuối tập tin ở trên\n",
        "def readFileWithName():\n",
        "    try:\n",
        "        # Nhập tên tập tin:\n",
        "        fileName3 = input(\"Mời bạn nhập vào tên tập tin: \")\n",
        "        # Nhập tên tập tin:\n",
        "        contentFile3 = input(\"Mời bạn nhập vào nội dung: \")\n",
        "        # Mở file:\n",
        "        file3 = open(f'{fileName3}.txt', \"a+\")\n",
        "        # Ghi nội dung vào file:\n",
        "        file3.write(contentFile3)\n",
        "        file3.close()\n",
        "        # Reading from file:\n",
        "        print(\"*********************************\")\n",
        "        output = open(f'{fileName3}.txt')\n",
        "        print(f'Nội dung file đã ghi là: {output.read()}')\n",
        "        print(\"*********************************\")\n",
        "        file3.close()\n",
        "    except:\n",
        "        print(\"File bị lỗi hoặc tên không tồn tại!\\nVui lòng nhập đúng tên file!\")\n",
        "        readFileWithName()\n",
        "readFileWithName()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z5bAIaKcPWlZ"
      },
      "source": [
        "# Bài 5: Viết chương trình thực các yêu cầu sau:\n",
        "# - Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng từ [-1000, 1000]\n",
        "# - Nhập tên tập tin từ bàn phím\n",
        "# - Ghi danh sách trên vào tập tin theo quy tắc:\n",
        "# o 10 số trên một hàng\n",
        "# o Các số phân tách nhau bởi dấu phẩy (,)\n",
        "# - Đọc nội dung tập tin ở trên và in ra màn hình theo quy tắc:\n",
        "# o 10 số trên một hàng\n",
        "# o Các số phan tách nhau bởi dấu tab.\n",
        "import random\n",
        "randomlist = [random.randrange(-1000, 10001) for i in range(0, 1000)]\n",
        "inputfile = input(\"Enter the name of file: \")\n",
        "\n",
        "#Open file write:\n",
        "fileName1 = open(inputfile, \"w\")\n",
        "for i in range(0, 100):\n",
        "    for j in range(0, 10):\n",
        "        if j == 0:\n",
        "            fileName1.write(str(randomlist[i*10 + j]))\n",
        "        else:\n",
        "            fileName1.write(str(randomlist[i*10 + j]) + \",\")\n",
        "    fileName1.write(\"\\n\")\n",
        "fileName1.close()\n",
        "#Open file to read:\n",
        "fileName2 = open(inputfile, \"r\")\n",
        "# file2 = open(\"xxx\", \"r\")\n",
        "valueOfline = fileName2.readline()\n",
        "while valueOfline != \"\":\n",
        "    newList = valueOfline.split(\",\")\n",
        "    newString = \"\\t\".join(newList)\n",
        "    print(newString)\n",
        "    valueOfline = fileName2.readline()\n",
        "fileName2.close()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}