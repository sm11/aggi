package com.example.loaner.aggi0


import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView


import android.support.v7.widget.DividerItemDecoration
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.Query
import com.mobymagic.easyfirebaselist.EmptyStyle
import com.mobymagic.easyfirebaselist.ErrorStyle
import com.mobymagic.easyfirebaselist.ProgressStyle
import com.mobymagic.easyfirebaselist.database.FirebaseDbListFragment
import com.thefinestartist.finestwebview.FinestWebView

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 *
 */
class NewsListFragment : FirebaseDbListFragment<News, NewsViewHolder>() {

    override fun getDataClass(): Class<News> {
        return News::class.java
    }

    override fun getEmptyStyle(): EmptyStyle {
        return EmptyStyle(R.drawable.ic_error_view_cloud, "No news yet in database")
    }

    override fun getErrorStyle(error: DatabaseError): ErrorStyle {
        return ErrorStyle(R.drawable.ic_error_view_cloud, "An error occurred while fetching news")
    }

    override fun getProgressStyle(): ProgressStyle {
        return ProgressStyle("Loading...")
    }

    override fun getQuery(): Query {
        return FirebaseDatabase.getInstance().reference.child("news").limitToLast(100)
    }

    override fun onBindViewHolder(viewHolder: NewsViewHolder, key: String, model: News) {
        viewHolder.bind(model)
    }

    override fun onCreateViewHolder(inflater: LayoutInflater, viewGroup: ViewGroup): NewsViewHolder {
        val view = inflater.inflate(R.layout.item_news, viewGroup, false)
        return NewsViewHolder(view)
    }

    override fun onItemClicked(viewHolder: NewsViewHolder, key: String, model: News) {
        FinestWebView.Builder(activity).show(model.link)
    }

    override fun setupRecyclerView(recyclerView: RecyclerView) {
        recyclerView.addItemDecoration(DividerItemDecoration(activity, DividerItemDecoration.VERTICAL))
        recyclerView.layoutManager = LinearLayoutManager(activity)
    }


}
