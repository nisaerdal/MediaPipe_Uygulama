def main():
    while True:
        choise_input = input("1:Hands Detection, 2:Pose Detection, 3:Holistic Detection =>")
        if choise_input == '1':
            from hands_detection import HandsDetection
            detector = HandsDetection()
            break

        elif choise_input == '2':
            from pose_detection import PoseDetection
            detector = PoseDetection()
            break

        elif choise_input == '3':
            from holistic_detection import HolisticDetection
            detector = HolisticDetection()
            break
        else:
            print('Tekrar input gir lütfen!')
            return

if __name__ == '__main__':
    main()

