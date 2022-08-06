import React from "react";
import OrdersTab from './OrdersTab';

class OrderManager extends React.Component{
    constructor(){
        super();
        this.state ={
            showHideTab1:true,
            showHideTab2:false,
            showHideTab3:false,
            showHideTab4:false,
            showHideTab5:false,
        }
        this.hideComponent = this.hideComponent.bind(this);
    }
    hideComponent(name){
        switch(name){
            case "showHideTab1":
                this.setState({showHideTab1:true,showHideTab2:false,showHideTab3:false,showHideTab4:false,showHideTab5:false});
                break;
            case "showHideTab2":
                this.setState({showHideTab1:false,showHideTab2:true,showHideTab3:false,showHideTab4:false,showHideTab5:false});
                break;
            case "showHideTab3":
                this.setState({showHideTab1:false,showHideTab2:false,showHideTab3:true,showHideTab4:false,showHideTab5:false});
                break;
            case "showHideTab4":
                this.setState({showHideTab1:false,showHideTab2:false,showHideTab3:false,showHideTab4:true,showHideTab5:false});
                break;
            case "showHideTab5":
                this.setState({showHideTab1:false,showHideTab2:false,showHideTab3:false,showHideTab4:false,showHideTab5:true});
                break;
        }
    }
    render(){
        const {showHideTab1,showHideTab2,showHideTab3,showHideTab4,showHideTab5} = this.state;
        return (
            <div className="OrderManager">
                <ul className="nav nav-tabs" id="myTab" role="tablist">
                    <li className="nav-item">
                        <button onClick={()=>this.hideComponent("showHideTab1")} className="nav-link active" id="pending-tab" data-bs-toggle="tab" data-bs-target="#pending" type="button" role="tab" aria-controls="pending" aria-selected="true">
                            Pending
                        </button>
                    </li>
                    <li className="nav-item">
                        <button onClick={()=>this.hideComponent("showHideTab2")} className="nav-link" id="inprocess-tab" data-bs-toggle="tab" data-bs-target="#inprocess" type="button" role="tab" aria-controls="inprocess" aria-selected="false">
                            In Process
                        </button>
                    </li>
                    <li className="nav-item">
                        <button onClick={()=>this.hideComponent("showHideTab3")} className="nav-link" id="completed-tab" data-bs-toggle="tab" data-bs-target="#completed" type="button" role="tab" aria-controls="completed" aria-selected="false">
                            Completed
                        </button>
                    </li>
                    <li className="nav-item">
                        <button onClick={()=>this.hideComponent("showHideTab4")} className="nav-link" id="delivered-tab" data-bs-toggle="tab" data-bs-target="#delivered" type="button" role="tab" aria-controls="delivered" aria-selected="false">
                            Delivered
                        </button>
                    </li>
                    <li className="nav-item">
                        <button onClick={()=>this.hideComponent("showHideTab5")} className="nav-link" id="canceled-tab" data-bs-toggle="tab" data-bs-target="#canceled" type="button" role="tab" aria-controls="canceled" aria-selected="false">
                            Canceled
                        </button>
                    </li>
                </ul>

                <div className="tab-content" id="myTabContent">
                    <div className="tab-pane fade show active" id="pending" role="tabpanel" aria-labelledby="pending-tab">
                    {showHideTab1 && <OrdersTab status="Pending" nextStatus="In Process"></OrdersTab> }
                    </div>

                    <div className="tab-pane fade" id="inprocess" role="tabpanel" aria-labelledby="inprocess-tab">
                    {showHideTab2 && <OrdersTab status="In Process" nextStatus="Completed"></OrdersTab> }
                    </div>

                    <div className="tab-pane fade" id="completed" role="tabpanel" aria-labelledby="completed-tab">
                    {showHideTab3 && <OrdersTab status="Completed" nextStatus="Delivered"></OrdersTab> }
                    </div>  

                    <div className="tab-pane fade" id="delivered" role="tabpanel" aria-labelledby="delivered-tab">
                    {showHideTab4 && <OrdersTab status="Delivered" nextStatus=""></OrdersTab>} 
                    </div>


                    <div className="tab-pane fade" id="canceled" role="tabpanel" aria-labelledby="canceled-tab">    
                    {showHideTab5 && <OrdersTab status="Canceled" nextStatus=""></OrdersTab> }
                    </div>

                </div>
            </div>

        );
    };
}

export default OrderManager;