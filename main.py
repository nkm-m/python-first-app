import os
import csv


def main():
    # inputで名前を聞く
    name = input("こんにちは！私はRobokoです。あなたの名前は何ですか？\n")
    print()

    try:
        # CSVファイルの存在チェック
        if os.path.exists("ranking.csv"):
            # CSVファイルの中身を引っ張ってくる
            with open("ranking.csv", "r") as csv_file:
                reader = csv.DictReader(csv_file)

                restaurants = []
                rows = []
                # 後で上書きするため、csvデータの保持
                for row in reader:
                    restaurants.append(row["Name"])
                    rows.append({"Name": row["Name"], "Count": row["Count"]})

                # カウント降順にソート
                sorted_rows = sorted(
                    rows, key=lambda row: row["Count"], reverse=True)

                # ソート順にオススメ
                for sorted_row in sorted_rows:
                    answer = input(
                        f"私のオススメのレストランは、{sorted_row['Name']}です。\nこのレストランは好きですか？[Yes/No]\n")
                    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
                        with open("ranking.csv", "w", newline="") as csv_file:
                            fieldnames = ["Name", "Count"]
                            writer = csv.DictWriter(
                                csv_file, fieldnames=fieldnames)
                            writer.writeheader()
                            # csvファイルの上書き
                            for row in rows:
                                # yesと答えた場合は、対象店のカウントを増やす
                                if row["Name"] == sorted_row['Name']:
                                    count = int(row["Count"])
                                    count += 1
                                    writer.writerow(
                                        {"Name": row["Name"], "Count": count})
                                # カウントを増やさずにcsvに上書き
                                else:
                                    writer.writerow(
                                        {"Name": row["Name"], "Count": row["Count"]})
                        break

                    elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
                        pass
                    else:
                        raise ValueError("YesかNoで入力してください。")

                restaurant = input(f"{name}さん。どこのレストランが好きですか？\n")
                restaurant = restaurant.title()

                # 初めての店名を登録
                with open("ranking.csv", "a", newline="") as csv_file:
                    fieldnames = ["Name", "Count"]
                    writer = csv.DictWriter(
                        csv_file, fieldnames=fieldnames)
                    writer.writerow({"Name": restaurant, "Count": 1})

        # 初回CSVファイル作成
        else:
            # レストランを聞く
            restaurant = input(f"{name}さん。どこのレストランが好きですか？\n")
            restaurant = restaurant.title()
            print()
            with open("ranking.csv", "w", newline="") as csv_file:
                fieldnames = ["Name", "Count"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({"Name": restaurant, "Count": 1})

            # メッセージを表示して終了
        print(f"{name}さん。ありがとうございました。\nよい一日を！さようなら。")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
