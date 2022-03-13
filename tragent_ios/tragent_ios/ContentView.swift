//
//  ContentView.swift
//  tragent_ios
//
//  Created by Sophia Tang on 8/18/21.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        Text("Tragent")
            .font(.title)
            .fontWeight(.heavy)
            .foregroundColor(Color.gray)
            .lineLimit(nil)
            .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
                
        }
    }
}
