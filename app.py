def main():
    choise_input = input("1:Hands Detection, 2:Pose Detection, 3:Holistic Detection =>")

    if choise_input == '1':
        from hands_detection import HandsDetection
        detector = HandsDetection()
        #hands_detector.run_detection()

    elif choise_input == '2':
        from pose_detection import PoseDetection
        detector = PoseDetection()

    elif choise_input == '3':
        pass

    else:
        print('Tekrar input gir lütfen!')

if __name__ == '__main__':
    main()

